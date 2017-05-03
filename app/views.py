# -*- coding: utf-8 -*-
from flask import render_template, request
from app import app
from .settings import hosts, password
from .fabfile import change_proxy


@app.route('/')
@app.route('/index')
def index():
    return render_template(
        'index.html',
        hosts=hosts)


@app.route('/change_ip', methods=['POST'])
def change_ip():
    host_name = request.form.get('hostname')
    host_ssh = get_host_ssh(host_name)
    if not host_ssh:
        return '未知主机'
    changed_ip = change_proxy([host_ssh], password).get(host_ssh, '更换ip失败')
    print host_ssh, changed_ip
    return changed_ip


def get_host_ssh(host_name):
    if not host_name:
        return None
    for host in hosts:
        if host['name'] == host_name:
            return host['ssh']
    return None
