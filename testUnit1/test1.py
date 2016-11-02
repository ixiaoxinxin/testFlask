import flask
from flask import request
from flask import make_response

app = flask.Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User_agent')
    #return '<p>your browser is %s</p>' % user_agent
    #return '<p>bad request</p>' ,400
    response = make_response('<h1>this document carries a cookie</h1>')
    response.set_cookie('awser','42')
    return response
@app.route('/user/<name>')
def user(name):
    return '<h1>hello,%s!</h1>' % name


if __name__ == '__main__':
    app.run(debug=True)
