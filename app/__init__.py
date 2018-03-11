# -*- coding: utf-8 -*-
# @Time :   2018/3/12
# @Author   :   Greendev
# @Project  : The_Flask_Mega-Tutorial
# @File :   __init__.py


from flask import Flask

app = Flask(__name__)

from app import routes
