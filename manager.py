#coding:utf-8

from werkzeug.utils import secure_filename
from flask.ext.script import Manager
from app import create_app

app = create_app()
manager = Manager(app)

# 能及时debug信息，自动更新到浏览器上显示
@manager.command
def dev():
    from livereload import Server
    live_server = Server(app.wsgi_app)
    # 监控所有的文件
    live_server.watch('**/*.*')
    live_server.serve(open_url=False)


@manager.command
def test():
    pass


@manager.command
def deploy():
    pass

if __name__ == '__main__':
    manager.run()