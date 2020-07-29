"""
Project name: flask_web
Description:
Create Time: 2020/7/28 08:41
Author: to2bage
Email: to2bage@hotmail.com
Version: 0.1
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_application():
    app = Flask(__name__)
    # 注册配置
    app.config.from_object("app.config.secret")
    app.config.from_object("app.config.settings")
    # 注册蓝图
    register_blueprint(app)
    # 添加数据库
    db = SQLAlchemy(app)
    db.init_app(app)
    db.create_all(app=app)

    return app

def register_blueprint(app: Flask):
    from app._response._cookie import bp_cookie

    app.register_blueprint(bp_cookie, url_prefix="/cookie")