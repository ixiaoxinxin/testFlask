from flask import  Flask
#程序制定的参数,程序主模块或包的名字__name__
#通过这个决定程序的根目录
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>hello world<h1>'