# -*- coding: utf-8 -*-

from .import admin
from flask import render_template


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
@admin.route("/tag/add/1/")
def tag_add():
    return render_template('./3-admin/tag_add.html')
    pass


@admin.route("/tag/list/<int:p>/")
def tag_list(p):
    print(p)
    return render_template('./3-admin/tag_list.html')
    pass


# 电影
@admin.route("/movie/add/1/")
def movie_add():
    return render_template('./3-admin/movie_add.html')
    pass


@admin.route("/movie/list/<int:p>/")
def movie_list(p):
    print(p)
    return render_template('./3-admin/movie_list.html')
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
@admin.route("/role/add/1/")
def role_add():
    return render_template('./3-admin/role_add.html')
    pass


@admin.route("/role/list/<int:p>/")
def role_list(p):
    print(p)
    return render_template('./3-admin/role_list.html')
    pass


# 权限
@admin.route("/auth/add/1/")
def auth_add():
    return render_template('./3-admin/auth_add.html')
    pass


@admin.route("/auth/list/<int:p>/")
def auth_list(p):
    print(p)
    return render_template('./3-admin/auth_list.html')
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
@admin.route("/admin/add/1/")
def admin_add():
    return render_template('./3-admin/admin_add.html')
    pass


@admin.route("/admin/list/<int:p>/")
def admin_list(p):
    print(p)
    return render_template('./3-admin/admin_list.html')
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
@admin.route('/preview/add/1/')
def preview_add():
    return render_template('./3-admin/preview_add.html')
    pass


@admin.route('/preview/list/<int:p>/')
def preview_list(p):
    print(p)
    return render_template('./3-admin/preview_list.html')
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

