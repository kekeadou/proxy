# -*- coding: utf-8 -*-
from flask import render_template, request, Response
from app import app
from settings import hosts


@app.route('/')
@app.route('/index')
def index():
    return render_template(
        'index.html',
        hosts=hosts)


@app.route('/change_ip', methods=['POST'])
def change_ip():
    hostname=request.args.get('hostname')
    if hostname=='123':
        resp = Response("192.168.1.1")
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    else:
        resp = Response("192.168.1.2")
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

