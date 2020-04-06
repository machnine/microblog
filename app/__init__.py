from flask import Flask
from config import Config

app = Flask(__name__)   #app = name of the Flask instance
app.config.from_object(Config)

from app import routes  #app = ..\app package
