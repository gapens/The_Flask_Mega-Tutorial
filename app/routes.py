# -*- coding: utf-8 -*-
# @Time :   2018/3/12
# @Author   :   Greendev
# @Project  : The_Flask_Mega-Tutorial
# @File :   routes.py


from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
