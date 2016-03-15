#coding:utf-8
from flask import Flask,render_template,request,redirect,url_for,make_response,abort
from werkzeug.routing import BaseConverter
from werkzeug.utils import secure_filename
from os import path
from flask.ext.script import Manager
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *

class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]

app = Flask(__name__)
app.url_map.converters['regex'] = RegexConverter

Bootstrap(app)
nav = Nav()
manager = Manager(app)
nav.register_element('top',Navbar(u'Flask入门',
                                  View(u'主页', 'index'),
                                  View(u'关于', 'about'),
                                  View(u'服务', 'services'),
                                  View(u'项目', 'projects')
                                ))
nav.init_app(app)

@app.route("/")
def index():
    return render_template("index.html",
                           title="<h1>Hello world</h1>",
                           body="# Header2")

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

@app.route('/login',methods=['GET','POST'])
def login():
    # if request.method == 'POST':
    #     username = request.form['username']
    #     password = request.form['password']
    # else:
    #     username = request.args['username']
    return render_template('login.html', method=request.method)

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

# 能及时debug信息，自动更新到浏览器上显示
@manager.command
def dev():
    from livereload import Server
    live_server = Server(app.wsgi_app)
    # 监控所有的文件
    live_server.watch('**/*.*')
    live_server.serve(open_url=True)

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

if __name__ == "__main__":
    # app.run(debug=True)
    manager.run()
