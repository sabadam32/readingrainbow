from flask import Flask
from .extensions import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cat.sqlite3'
    
    db.init_app(app)

    return app