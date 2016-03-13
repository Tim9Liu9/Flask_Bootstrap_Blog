#coding:utf-8
from flask import Flask,render_template,request
from werkzeug.routing import BaseConverter

class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]

app = Flask(__name__)
app.url_map.converters['regex'] = RegexConverter

@app.route("/")
def hello():
    # return "<h3>Hello world!</h3>"
    return render_template('index.html',title='wecome')

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
    return render_template('login.html', method=request.method)

if __name__ == "__main__":
    app.run(debug=True)
