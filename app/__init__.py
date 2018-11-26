from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='../back/templates')
app.config.from_object('settings')
db = SQLAlchemy(app)

from back import views
