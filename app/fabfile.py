# -*- coding: utf-8 -*-
from fabric.api import cd, env, run, parallel, execute, hide
from fabric.api import settings as api_settings
import re
import time

retry_times = 3


@parallel(pool_size=5)
def remote_change():
    remote_ip = ''
    with hide('output', 'running', 'warnings'), api_settings(warn_only=True):
        with cd('/data/deploy/client'):
            retry = 0
            while not remote_ip and retry < retry_times:
                ret = run('/bin/sh change_proxy.sh')
                m = re.search('IP：\s*(\d+\.\d+\.\d+\.\d+)', ret.strip(), re.M)
                remote_ip = m.group(1) if m else None
                print 'remote ip: ', remote_ip

                retry += 1
                if not remote_ip:
                    print 'remote change fail: ', retry
    return remote_ip


def change_proxy(hosts, password):
    env.password = password
    return execute(remote_change, hosts=hosts)


if __name__ == "__main__":
    from settings import hosts, password
    hosts = [host['ssh'] for host in hosts]
    env.password = password

    print change_proxy(hosts, password)
