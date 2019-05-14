# -*- coding: utf-8 -*-

from . import home
from flask import render_template,request


@home.route("/")
def index():
    return render_template('./2-movie/index.html')
    # return "<h1 style='color=:green'>this is home</h1>"


@home.route("/animation/")
def animation():
    return render_template('./1-index-animation/animation.html')
    pass


@home.route("/play/<string:uuid>/")
def play(uuid):
    print(uuid)
    return render_template('./2-movie/play.html')
    pass


@home.route("/search/<string:key>/")
def search(key):
    print(key)
    return render_template('./2-movie/search.html')
    pass


@home.route("/login/")
def login():
    return render_template('./2-movie/login.html')
    pass


@home.route("/register/")
def register():
    return render_template('./2-movie/register.html')
    pass


@home.route("/user/<string:uuid>/")
def user(uuid):
    print(uuid)
    return render_template('./2-movie/user.html')
    pass


@home.route('/pwd/')
def pwd():
    return render_template('./2-movie/pwd.html')
    pass


@home.route('/moviecol/')
def moviecol():
    return render_template('./2-movie/moviecol.html')
    pass


# 登陆日志
@home.route('/loginlog/')
def loginlog():
    return render_template('./2-movie/loginlog.html')
    pass


# 评论记录
@home.route('/comments/')
def comments():
    return render_template('./2-movie/comments.html')
    pass
