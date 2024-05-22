from ..extensions import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    author = db.Column(db.String(50))
    publish_date = db.Column(db.DateTime)
    category = db.Column(db.Integer)