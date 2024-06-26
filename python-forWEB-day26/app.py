from flask import Flask,render_template,request, redirect, url_for
import os
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
@app.route('/')
def home():
  ##  return'<h1>hello myHome<h1>'
    #return render_template('home.html')
   # return '<ul><li><a href="/">Home</a></li><li><a href="/about">About</a></li></ul>'
    techs = ['python','java','c++','c#']
    name = 'mohamed'
    return render_template('home.html',techs=techs,name=name,title='myHome')
@app.route('/about')
def about():
   # return'<h1>about<h1>'
   #return render_template('about.html')
   name = 'the is about'
   return render_template('about.html',name=name)
@app.route('/result')
def result():
   return render_template('result.html')
@app.route('/post',methods=['GET','POST'])
def post():
    #return render_template('post.html')
   #name = 'the is post'
    #return render_template('post.html',name=name)
    name = 'the is post'
    if request.method == 'POST':
        name = request.form['name']
        return render_template('post.html',name=name)
    if request.method == 'GET':
        content = request.args.get('content')
        print(content)
        return redirect(url_for('result'))
        


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5001)))

    