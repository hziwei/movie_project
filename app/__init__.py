# -*- coding: utf-8 -*-

from flask import Flask


app = Flask(__name__)
app.debug = True
app.config.update(TEMPLATE_AUTO_RELOAD=True)
app.config['SECRET_KEY'] = '123456'
app.secret_key = b'\xd6\x19\xd6\xd9\x97\xa45\x99\x86\xa4\xc8I\xfcS\x10\x16\x11\xc04\xce\x0c\x18\xa2\x93'
from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")


