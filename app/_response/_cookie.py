"""
Project name: flask_web
Description:
Create Time: 2020/7/29 09:06
Author: to2bage
Email: to2bage@hotmail.com
Version: 0.1
"""
from flask import make_response
from flask import request
from flask import jsonify, Response, Request
from flask import session

from flask import Blueprint


bp_cookie = Blueprint("resp", __name__)

@bp_cookie.route("/setcookie")
def set_cookie():
    response: Response = make_response("设置COOKIES")
    response.mimetype = "text/plain"
    response.set_cookie("name", "to2bage", max_age=3600)
    return response, 200
    pass

@bp_cookie.route("/getcookie")
def get_cookie():
    print(request.cookies)
    return jsonify(request.cookies)

@bp_cookie.route("/setsession")
def set_session():
    session.permanent = True
    session["user"] = "to2bage"
    return "success"

@bp_cookie.route("/getsession")
def get_session():
    return session.get("user", "have nothong on...")
