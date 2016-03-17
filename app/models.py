#coding:utf-8



from . import db


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    users = db.relationship('User', backref='role')

    @staticmethod
    def seed():
        db.session.add_all(map(lambda r: Role(name=r), ['Guests','Administrators']))
        db.session.commit()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    password = db.Column(db.String, nullable=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @staticmethod
    def on_created(target, value, initiator):
        target.role = Role.query.filter_by(name='Guests') .first()

db.event.listen(User.name, 'set', User.on_created)



'''

#python manager.py shell

>>> from app import db
>>> from app import models
>>> db.create_all()

>>> from app.models import Role,User
>>> admins=Role(name='administrators')
>>> mod=Role(name='moderator')
>>> db.session.add_all([admins,mod])
>>> db.session.commit()

>>> tim = User(name='Tim', role=admins)
>>> db.session.add(tim)
>>> db.session.commit()


 tim.password = '123456'
>>> db.session.add(tim)
>>> db.session.commit()

>>> db.session.delete(tim)
>>> db.session.commit()

>>> db.session.add(User(name='Tim', role=admins))
>>> db.session.commit()

>>> User.query.all()
>>> User.query.get(1)

>>> Role.query.get(1)
>>> Role.query.get(2)
>>> Role.query.get(3)
>>> Role.query.get(2).name

'''

'''
15-数据库事件与数据迁移
 安装数据迁移插件：#pip install flask-migrate
数据库初始化环境，生成相应的文件migrations夹里面的内容： #python manager.py db init
初始化的迁移，生成migrations/versions/里面的文件： #python manager.py db migrate -m 'Initial migration'
迁移生成数据库文件(删除以前的相关表)：#python manager.py db upgrade
迁移生成数据库文件(重新建立以前的相关表)：#python manager.py db downgrade

应该有问题：
执行下面命令只会删除以前的数据表
#python manager.py db upgrade
应该还要执行下面的命令，来生成相关的数据表：
#python manager.py db downgrade
那么​manage.py里面的deploy()方法也是有问题的，正确的是如下：
@manager.command
def deploy():
    from app.models import Role
    upgrade()
    downgrade()
    Role.seed()
'''