#import Flask class from flask module
from flask import Flask

#import config class from the config.py in the same folder as microblog.py
from config import Config

#app = name of the Flask instance
app = Flask(__name__)   
#read app (instance) config
app.config.from_object(Config)

#from the ..\app folder import routes.py
from app import routes  
