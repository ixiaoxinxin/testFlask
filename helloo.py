from flask import Flask, render_template, session, redirect, url_for, flash
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy
from flask_script import Shell
from flask_migrate import Migrate, MigrateCommand
from flask_mail import Mail, Message
import os
from threading import Thread

app = Flask(__name__)
db = SQLAlchemy(app)
manager = Manager(app)
bootstrap = Bootstrap(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
mail = Mail(app)
#========================================================
basedir = os.path.abspath(os.path.dirname(__file__))
#=========================================================
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
#app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True #noneed
app.config['SQLALCHEMY_TRACK_MODIFICATIONS '] = True
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('shhhdkjqfbogbihi')
app.config['FLASKY_MAIL_SUBJECT_PREDIX'] = ['Flasky']
app.config['FLASY_MAIL_SENDER'] = 'Flasky admin<295563386@qq.com>'
app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')


def send_async_email(app,msg):
    with app.app_context():
        mail.send(msg)


def send_mail(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREDIX'] + subject, sender=app.config['FLASKY_MAIL_SENDER'], recipients =[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)
    thr = Thread(target=send_async_email, args=[app.msg])
    thr.start()
    return thr


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    user = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))


class NameForm(FlaskForm):
    name = StringField('what is your name?', validators=[Required()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    #name = None
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        #old_name = session.get('name')
        #if old_name is not None and old_name != form.name.data:
            #flash('looks like you have changed your name!')
        #session['name'] = form.name.data
        #form.name.data = ''
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
            if app.config['FLASKY_ADMIN']:
                send_mail(app.config['FLASKY_ADMIN'],'New User','mail/new_user',user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data=''
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False))


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

def make_shell_context():
    return dict(app=app, db=db, User=User,Role=Role)
manager.add_command("shell", Shell(make_context=make_shell_context))


if __name__ == '__main__':
    app.run(debug=True)
