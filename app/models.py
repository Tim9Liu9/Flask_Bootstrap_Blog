#coding:utf-8



from . import db


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    users = db.relationship('User', backref='role')


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    password = db.Column(db.String, nullable=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))




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