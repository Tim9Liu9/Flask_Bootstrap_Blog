#coding:utf-8

from werkzeug.utils import secure_filename
from flask.ext.script import Manager
from app import create_app, db
from flask_migrate import Migrate, MigrateCommand,upgrade,downgrade

app = create_app()
manager = Manager(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

# 能及时debug信息，自动更新到浏览器上显示
@manager.command
def dev():
    from livereload import Server
    live_server = Server(app.wsgi_app)
    # 监控所有的文件
    live_server.watch('**/*.*')
    live_server.serve(open_url=True)


@manager.command
def test():
    pass


# 数据迁移工作：其实是执行：migrations/versions里面的py文件
@manager.command
def deploy():
    from app.models import Role
    upgrade()
    downgrade()
    Role.seed()

if __name__ == '__main__':
    manager.run()