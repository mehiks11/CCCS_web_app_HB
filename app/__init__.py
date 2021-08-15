from flask import Flask, session
from flask_basicauth import BasicAuth 
import flask_login

#create app
app = Flask(__name__)

#pull in config file for dev. (**Switched to production if deployed in production**)
if app.config['ENV'] == 'producttion':
    app.config.from_object('config.ProductionConfig')
else:
    app.config.from_object('config.DevelopmentConfig')


from app import views
from app import admin_views


