import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return '<h1>hello world<h1>'



if __name__ == '__main__':
    app.run(debug=True)

#tesr
















