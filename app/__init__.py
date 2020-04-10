from flask import Flask                 #import Flask class from flask module
from config import Config               #import config class from the config.py in the same folder as microblog.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)                   #app = name of the Flask instance
app.config.from_object(Config)          #read app (instance) config
db = SQLAlchemy(app)                    #database object
migrate = Migrate(app,db)               #db migration object

from app import routes, models          #from the ..\app folder import routes.py

