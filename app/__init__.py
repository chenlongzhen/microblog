from flask import Flask

app = Flask(__name__)
app.config.from_object('app.config')
#app.config.from_pyfile('config')

from app import views