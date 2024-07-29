from flask import Flask,url_for,render_template
from markupsafe import escape

app = Flask(__name__)
@app.route('/')

def hello_world():
    return 'hello world'

@app.route('/user/<name>')
def usr_pag(name):
    return f'Usr:{escape(name)}'

@app.route('/test')
def test_url_for():
    print(url_for('hello_world'))
    print(url_for('usr_pag', name='greyli'))
    print(url_for('usr_pag', name='peter'))  # 输出：/user/peter
    print(url_for('test_url_for'))  # 输出：/test
    # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL 后面。
    print(url_for('test_url_for', num=2))  # 输出：/test?num=2
    return 'Test page'
name = 'Grey Li'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]

@app.route('/movie')
def index():
    return render_template('index.html', movies=movies)


