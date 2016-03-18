#coding:utf-8

from flask import Flask
from werkzeug.routing import BaseConverter

from os import path
from flask.ext.script import Manager
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
from flask_sqlalchemy import SQLAlchemy


# class RegexConverter(BaseConverter):
#     def __init__(self, url_map, *items):
#         super(RegexConverter, self).__init__(url_map)
#         self.regex = items[0]

basedir = path.abspath(path.dirname(__file__))
# print "000====>2,basedir=%s" % basedir



bootstrap = Bootstrap()
nav = Nav()


db = SQLAlchemy()



def create_app():
    app = Flask(__name__)
    # app.url_map.converters['regex'] = RegexConverter
    app.config.from_pyfile('config')
    app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

    nav.register_element('top',Navbar(u'Flask入门',
                                  View(u'主页', 'index'),
                                  View(u'关于', 'about'),
                                  View(u'服务', 'services'),
                                  View(u'项目', 'projects')
                                ))
    # 用了蓝图后：base.html里面的
    '''
    {% block navbar %}
        {{ nav.top.render() }}

    {% endblock %} 会出错
    '''
    db.init_app(app)
    bootstrap.init_app(app)

    nav.init_app(app)
    # init_views(app)

    from auth import auth as auth_blueprint
    from main import main as main_blueprint

    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    # app.register_blueprint(main_blueprint, static_folder='static')
    app.register_blueprint(main_blueprint)



    return app











# if __name__ == "__main__":
    # app.run(debug=True)
    # manager.run()
    # print "000====>1"
    # dev()
