from flask import request
from flask import make_response
from flask import Flask
from flask import render_template
from flask_bootstrap3 import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    #user_agent = request.headers.get('User_agent')
    #return '<p>your browser is %s</p>' % user_agent
    #return '<p>bad request</p>' ,400
    #response = make_response('<h1>this document carries a cookie</h1>')
    #response.set_cookie('awser','42')
    #return response
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    #return '<h1>hello,%s!</h1>' % name
    return render_template('user.html', name)


if __name__ == '__main__':
    app.run(debug=True)
