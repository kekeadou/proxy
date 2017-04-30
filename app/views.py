# -*- coding: utf-8 -*-
from flask import render_template, request
from app import app
from settings import hosts, password
from fabfile import change_proxy


@app.route('/')
@app.route('/index')
def index():
    return render_template(
        'index.html',
        hosts=hosts)


@app.route('/change_ip', methods=['POST'])
def change_ip():
    host_name = request.form['name']
    host_ssh = None
    for host in hosts:
        if host['name'] == host_name:
            host_ssh = host['ssh']
            break
    if not host_ssh:
        return '没找到host对应的服务器'
    new_ip = change_proxy(host_ssh, password).get(host_name)
    if not new_ip:
        return '更换代理ip失败。'
    return new_ip
