# -*- coding: utf-8 -*-
from fabric.api import local, cd, run, env, parallel, execute
from settings import hosts, password

env.hosts = [host['ssh'] for host in hosts]
env.password = password


@parallel(pool_size=5)
def update():
    print 'remote update'
    with cd('/data/deploy'):
        run('ls -l|wc -l')


if __name__ == "__main__":
    execute(update)
