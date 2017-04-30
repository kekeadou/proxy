# -*- coding: utf-8 -*-
from flask import render_template, request
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
    #print request.form
    #return index()
    return "192.168.1.1"
