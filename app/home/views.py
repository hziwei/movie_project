# -*- coding: utf-8 -*-

from . import home
from flask import render_template, request, flash, redirect, url_for, session
from app.models import *
import time


@home.route("/")
def index():
    m_list = Movie.query.all()
    return render_template('./2-movie/index.html', m_list=m_list)
    # return "<h1 style='color=:green'>this is home</h1>"


@home.route("/animation/")
def animation():
    return render_template('./1-index-animation/animation.html')
    pass


@home.route("/play/<string:uuid>/")
def play(uuid):
    movie = Movie.query.all()
    return render_template('./2-movie/play.html', movie=movie[0])
    pass


@home.route("/search/<string:key>/")
def search(key):
    print(key)
    return render_template('./2-movie/search.html')
    pass


@home.route("/login/", methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        name = request.form['contact']
        pwd = request.form['password']
        use = User.query.filter_by(name=name, pwd=pwd).all()
        if use:
            session[name] = pwd
        use1 = User.query.filter_by(email=name, pwd=pwd).all()
        if use1:
            session[name] = pwd
        use2 = User.query.filter_by(phone=name, pwd=pwd).all()
        if use2:
            session[name] = pwd
            pass
        if not (use or use1 or use2):
            return redirect(url_for('home.login'))
        m_list = Movie.query.all()
        return render_template('./2-movie/index.html', use=use, m_list=m_list)
        pass
    return render_template('./2-movie/login.html')
    pass


@home.route("/register/", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        User.query.all()
        use = User()
        use.name = request.form['name']
        use.email = request.form['email']
        use.phone = request.form['phone']
        use.pwd = request.form['repassword']
        use.addtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        db.session.add(use)
        db.session.commit()
    return render_template('./2-movie/register.html')
    pass


@home.route("/user/<string:uuid>/")
def user(uuid):
    print(User.query.filter_by(id=2).all())
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
