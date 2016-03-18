#coding:utf-8

from flask import render_template, request, flash, redirect, url_for, make_response
from os import path
from werkzeug.utils import secure_filename

from . import main

@main.route("/")
def index():
    print "index-->"
    return render_template("index.html",title=u"欢迎")

@main.route('/about')
def about():
    return render_template("about.html",title=u"关于")



@main.route("/services")
def services():
    return 'services'








'''
 # 自定义404页面
@main.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")

@main.route('/user/<username>')
def user(username):
    return "User %s" % username

@main.route('/user2/<int:user_id>')
def user2(user_id):
    return "User_id: %d" % user_id

# 注意<>里面的空格，可能导致编译错误
@main.route('/user3/<regex("[a-z]{3}"):user_id>')
def user3(user_id):
    return "User_id: %s" % user_id

@main.route('/projects/')
@main.route('/our-works/')
def projects():
    return 'The project page'


# 演示文件上传到服务器
@main.route('/upload',methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = path.abspath(path.dirname(__file__))
        upload_path = path.join(basepath, 'static/uploads/')
        print f
        print upload_path
        f.save(upload_path + secure_filename(f.filename))
        return redirect(url_for('upload'))
    return render_template('upload.html')


@main.template_test('current_link')
def is_current_link(link):
    return link == request.path

@main.template_filter('md')
def markdown_to_html(txt):
    from markdown import markdown
    return markdown(txt)


def read_md(filename):
    with open(filename) as md_file:
        content = reduce(lambda x,y:x+y, md_file.readlines())
    return content.decode('utf-8')

@main.context_processor
def inject_methods():
    return dict(read_md=read_md)
'''