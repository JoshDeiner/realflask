''' render routes'''
from flask import render_template
import app
from app.forms import LoginForm


@app.app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign in', form=form)



@app.app.route("/")
@app.app.route("/index")
def index():

    ''' return html user info '''
    user = {"username": "miguel"}
    posts = [

        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
