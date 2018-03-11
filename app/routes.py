# -*- coding: utf-8 -*-
# @Time :   2018/3/12
# @Author   :   Greendev
# @Project  : The_Flask_Mega-Tutorial
# @File :   routes.py


from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello World!"