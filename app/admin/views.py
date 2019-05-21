# -*- coding: utf-8 -*-

from .import admin
from flask import render_template, request
from app.models import *

import datetime,time


@admin.route("/")
def admin_index():
    return render_template('./3-admin/admin.html')
    pass


@admin.route("/index/")
def index():
    return render_template('./3-admin/index.html')
    pass


@admin.route("/login/")
def login():
    return render_template('./3-admin/login.html')
    pass


# 标签
@admin.route("/tag/add/1/", methods=['POST', 'GET'])
def tag_add():
    if request.method == "POST":
        tag = Tag()
        tag.name = request.form['name']
        tag.addtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        db.session.add(tag)
        db.session.commit()
    return render_template('./3-admin/tag_add.html')
    pass


@admin.route("/tag/list/<int:p>/")
def tag_list(p):
    t_list = Tag.query.all()
    return render_template('./3-admin/tag_list.html', t_list=t_list)
    pass


# 电影
@admin.route("/movie/add/1/", methods=['POST', 'GET'])
def movie_add():
    t_list = Tag.query.all()
    if request.method == "POST":
        movie = Movie()
        movie.title = request.form['title']
        movie.url = request.form['url']
        movie.info = request.form['info']
        movie.logo = request.form['logo']
        movie.star = request.form['star']
        movie.tag_id = request.form['tag_id']
        movie.area = request.form['area']
        movie.length = request.form['length']
        movie.realese_time = request.form['realese_time']
        movie.addtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        try:
            db.session.add(movie)
            db.session.commit()
        except Exception as ex:
            print(ex.args)
        print(movie)
    return render_template('./3-admin/movie_add.html', t_list=t_list)
    pass


@admin.route("/movie/list/<int:p>/")
def movie_list(p):
    m_list = Movie.query.all()
    t_list = Tag.query.all()
    return render_template('./3-admin/movie_list.html', m_list=m_list, t_list=t_list)
    pass


# 会员
@admin.route("/user/add/1/")
def user_add():
    return render_template('./3-admin/user_add.html')
    pass


@admin.route("/user/list/<int:p>/")
def user_list(p):
    print(p)
    return render_template('./3-admin/user_list.html')
    pass


# 评论
@admin.route("/comment/add/1/")
def comment_add():
    return render_template('./3-admin/comment_add.html')
    pass


@admin.route("/comment/list/<int:p>/")
def comment_list(p):
    print(p)
    return render_template('./3-admin/comment_list.html')
    pass


# 角色
@admin.route("/role/add/1/", methods=['POST', 'GET'])
def role_add():
    a_list = Auth.query.all()
    if request.method == 'POST':
        role = Role()
        role.name = request.form['name']
        role.auths = ','.join(request.form.getlist('auths[]'))
        role.addtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        db.session.add(role)
        db.session.commit()
        pass
    return render_template('./3-admin/role_add.html',a_list=a_list)
    pass


@admin.route("/role/list/<int:p>/")
def role_list(p):
    r_list = Role.query.all()
    return render_template('./3-admin/role_list.html', r_list=r_list)
    pass


# 权限
@admin.route("/auth/add/1/", methods=['POST', 'GET'])
def auth_add():
    if request.method == 'POST':
        auth = Auth()
        auth.name = request.form['name']
        auth.url = request.form['url']
        auth.addtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        db.session.add(auth)
        db.session.commit()
        pass
    return render_template('./3-admin/auth_add.html')
    pass


@admin.route("/auth/list/<int:p>/")
def auth_list(p):
    a_list = Auth.query.all()
    return render_template('./3-admin/auth_list.html', a_list=a_list)
    pass


# 角色权限
@admin.route("/role/auth/add/1/")
def role_auth_add():
    return render_template('./3-admin/role_auth_add.html')
    pass


@admin.route("/role/auth/list/<int:p>/")
def role_auth_list(p):
    print(p)
    return render_template('./3-admin/role_auth_list.html')
    pass


# 管理员
@admin.route("/admin/add/1/",methods=['POST', 'GET'])
def admin_add():
    r_list = Role.query.all()
    if request.method == 'POST':
        admin = Admin()
        admin.name = request.form['name']
        admin.pwd = request.form['pwd']
        admin.role_id = request.form['role_id']
        admin.addtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        db.session.add(admin)
        db.session.commit()
        pass
    return render_template('./3-admin/admin_add.html', r_list=r_list)
    pass


@admin.route("/admin/list/<int:p>/")
def admin_list(p):
    r_list = Role.query.all()
    a_list = Admin.query.all()
    return render_template('./3-admin/admin_list.html', a_list=a_list, r_list=r_list)
    pass


# 管理员角色编辑


# 日志
@admin.route("/oplog/list/<int:p>/")
def oplog_add(p):
    print('log', p)
    return render_template('./3-admin/oplog_list.html')
    pass


@admin.route('/adminloginlog/list/<int:p>/')
def adminloginlog(p):
    return render_template('./3-admin/adminloginlog.html')
    pass


@admin.route('/userloginlog/list/<int:p>/')
def userloginlog_list(p):
    return render_template('./3-admin/userloginlog_list.html')
    pass


# 预告管理
@admin.route('/preview/add/1/', methods=['POST', 'GET'])
def preview_add():
    if request.method == "POST":
        previesw = Previesw()
        previesw.title = request.form['title']
        previesw.logo = request.form['logo']
        previesw.addtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        db.session.add(previesw)
        db.session.commit()
    return render_template('./3-admin/preview_add.html')
    pass


@admin.route('/preview/list/<int:p>/')
def preview_list(p):
    p_list = Previesw.query.all()
    return render_template('./3-admin/preview_list.html', p_list=p_list)
    pass


# 收藏
@admin.route('/moviecol/list/<int:p>/')
def moviecol_list(p):
    print(p)
    return render_template('./3-admin/moviecol_list.html')
    pass


# 修改密码页
@admin.route("/pwd/")
def pwd_list():
    return render_template('./3-admin/pwd.html')
    pass

