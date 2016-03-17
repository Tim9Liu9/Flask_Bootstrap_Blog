#coding:utf-8

from flask import Flask,render_template, redirect, make_response, flash,url_for,request
from os import path
from werkzeug.utils import secure_filename

def init_views(app):
    @app.route("/")
    def index():
        return render_template("index.html",
                               title="Welcome")

    # @app.route("/")
    def hello():
        # return "<h3>Hello world!</h3>"
        # abort(404)
        response = make_response(render_template('index.html',title='wecome'))
        # return render_template('index.html',title='wecome')
        response.set_cookie('username', '')
        return response

    @app.route("/services")
    def services():
        return 'services'

    @app.route('/about')
    def about():
        return 'About'

    @app.route('/user/<username>')
    def user(username):
        return "User %s" % username

    @app.route('/user2/<int:user_id>')
    def user2(user_id):
        return "User_id: %d" % user_id

    # 注意<>里面的空格，可能导致编译错误
    @app.route('/user3/<regex("[a-z]{3}"):user_id>')
    def user3(user_id):
        return "User_id: %s" % user_id

    @app.route('/projects/')
    @app.route('/our-works/')
    def projects():
        return 'The project page'

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        from app.forms import LoginForm
        form = LoginForm()
        flash(u"登录成功！")
        return render_template('login.html', title=u'登录', form=form)



    # 演示文件上传到服务器
    @app.route('/upload',methods=['GET','POST'])
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

    # 自定义404页面
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html")

    @app.template_test('current_link')
    def is_current_link(link):
        return link == request.path


    @app.template_filter('md')
    def markdown_to_html(txt):
        from markdown import markdown
        return markdown(txt)


    def read_md(filename):
        with open(filename) as md_file:
            content = reduce(lambda x,y:x+y, md_file.readlines())
        return content.decode('utf-8')

    @app.context_processor
    def inject_methods():
        return dict(read_md=read_md)
