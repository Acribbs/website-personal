from flask import render_template, flash, redirect, session,\
	url_for, request, g, request, Response, stream_with_context, request, Flask, \
	send_file, make_response
from flask_login import LoginManager, UserMixin, login_user, logout_user,\
    current_user
#from flask_sqlalchemy import SQLAlchemy
from flask_wtf import Form
from wtforms import StringField, widgets, SelectMultipleField, SelectField, RadioField
from wtforms.validators import DataRequired, Length, Optional
#from sqlalchemy import *
from sqlalchemy.orm import Session
from app import app, Models
from oauth import OAuthSignIn
from Models import bcrypt
import os
import re
import StringIO
import csv


# initialise a login manager and SQLAlchemy database
lm = LoginManager(app)

# not suing sqlite but may do in the future
#db = SQLAlchemy(app)

# Not using sqlite at the moment but for comments I may use them in the future
#engine = create_engine('sqlite:///csvdb')
#session = Session(bind=engine)



#Login manager

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
	
		
#Views and routes start here

from Models import User, csvdb, User2


#Facebook/Twitter user loader - This may be used in the future for blog comments

'''
@login_manager.user_loader
def load_user(id):
	if hasrun == True:
		global hasrun
		hasrun = False
		return User2.query.get(int(id))
	else:
		return User.query.get(int(id))
@lm.user_loader
def load_user(id):
	if hasrun == True:
		global hasrun
		hasrun = False
		return User2.query.get(int(id))
	else:
		return User.query.get(int(id))
'''
########################

# route start here

@app.route('/')
def home():
    return render_template('Home.html')
    

@app.route('/home')
def index():
    return render_template('Home.html')
    

@app.route('/Science')
def Publications():
	return render_template('Science.html')

@app.route('/Code')
def Example_code():
	return render_template('Code.html')

@app.route('/Blog')
def Blog():
    return render_template('blog-index.html')

@app.route('/Contact')
def Contact():
	return render_template('Contact.html')

# Where the blog routes start:

@app.route('/python-start')
def Pythonstart():
    return render_template('blog/python-start.html')
    

@app.route('/python-pandas')
def Pythonpandas():
    return render_template('blog/python-pandas.html')

@app.route('/ipython_notebook')
def IpythonNotebook():
    return render_template('blog/ipython_notebook.html')

@app.route('/ipython_notebook2')
def IpythonNotebook2():
    return render_template('blog/ipython_notebook2.html')

@app.route('/gittutorial')
def Gittutorial():
    return render_template('blog/Gittutorial.html')
    
@app.route('/scripts')
def Scripts():
    return render_template('blog/scripts.html')

@app.route('/github')
def Github():
    return render_template('blog/github.html')

@app.route('/language')
def Language():
    return render_template('blog/language.html')    


    
    
# Method of the month
@app.route('/Method-1')
def MethodOne():
    return render_template('blog/Method-1.html')

@app.route('/Method-2')
def MethodTwo():
    return render_template('blog/Method-April17.html')
    
    
# Featured code tutorial

@app.route('/bash-tutorial1')
def BashOne():
    return render_template('code/bash-tutorial1.html')

@app.route('/softlink')
def Softlink():
    return render_template('code/Softlink+files.html')
@app.route('/softlink1')
def Softlink1():
    return render_template('code/Softlink.html')

@app.route('/ensembl')
def Ensembl():
	return render_template('code/ensembl.html')

@app.route('/ensembl1')
def Ensembl1():
	return render_template('code/Ensemble_to_gene_symbol.html')




@app.after_request
def add_header(response):
    response.cache_control.max_age = 300
    return response

@app.route('/google0daab0556399ff0b.html')
def Google():
    return render_template('google0daab0556399ff0b.html') 
    
@app.route('/sitemap.xml')
def Sitemap():
    return render_template('sitemap.xml') 

@app.route('/BingSiteAuth.xml')
def Sitemap():
    return render_template('BingSiteAuth.xml') 


#Flask login route - This may be enabled in the future for blog posting comments - but at the moment
#the code can be disabled

'''
@app.route('/register' , methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    user = User2(request.form['username'] , request.form['password'],request.form['email'])
    db.session.add(user)
    db.session.commit()
    flash('User successfully registered')
    return redirect(url_for('login'))

global hasrun
hasrun = False
	  
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form['username']
    password = request.form['password']
    registered_user = User2.query.filter_by(username=username).first()
    if registered_user is None:
        flash('Username is invalid' , 'error')
        return redirect(url_for('login'))
    if bcrypt.check_password_hash(registered_user.password, password) == True:
    	login_user(registered_user)
    else:
    	flash('Password is invalid' , 'error')
        return redirect(url_for('login'))
    global hasrun
    hasrun = True
    return redirect(request.args.get('next') or url_for('index'))
'''
