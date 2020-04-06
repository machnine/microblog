from flask import Flask

app = Flask(__name__)   #app = name of the Flask instance

from app import routes  #app = ..\app package
