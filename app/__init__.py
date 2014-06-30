from flask import Flask

app = Flask(__name__)
app.config.from_oject('config')

from app import views
