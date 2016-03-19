# coding=utf-8

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask.ext.pagedown.fields import PageDownField


class PostForm(Form):
    title = StringField(label=u"标题", validators=[DataRequired()])
    body = PageDownField(label=u"正文", validators=[DataRequired()])
    submit = SubmitField(u"发表")


class CommentForm(Form):
    body = PageDownField(label=u'评论', validators=[DataRequired()])
    submit = SubmitField(u'发表')
