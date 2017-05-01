# -*- coding: utf-8 -*-
from fabric.api import cd, env, run, parallel, execute, hide, settings
import re
import time

retry_times = 3


@parallel(pool_size=5)
def remote_change():
    remote_ip = None
    with hide('output', 'running', 'warnings'), settings(warn_only=True):
        with cd('/data/deploy/client'):
            ret = run('/bin/sh change_proxy.sh')
            retry = 0
            while ret.failed and retry < retry_times:
                ret = run('/bin/sh change_proxy.sh')
                retry += 1
                time.sleep(5)
            if ret:
                remote_ip = re.search('IP：\s*(\d+\.\d+\.\d+\.\d+)', ret.strip()).group(1)
    return remote_ip


def change_proxy(hosts, password):
    return execute(remote_change, hosts=hosts)


if __name__ == "__main__":

    from settings import hosts, password
    hosts = [host['ssh'] for host in hosts]
    env.password = password

    print change_proxy(hosts, password)
