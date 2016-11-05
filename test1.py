from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_script import Manager
from flask.ext.moment import Moment

app = Flask(__name__)
bootstrap = Bootstrap(app)
manager = Manager(app)
moment = Moment(app)
from datetime import datetime

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500

@app.route('/')
def index():
    #user_agent = request.headers.get('User_agent')
    #return '<p>your browser is %s</p>' % user_agent
    #return '<p>bad request</p>' ,400
    #response = make_response('<h1>this document carries a cookie</h1>')
    #response.set_cookie('awser','42')
    #return response
    return render_template('index.html',
                           current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    #return '<h1>hello,%s!</h1>' % name
    return render_template('user.html', name=name)

if __name__ == '__main__':
    app.run()
