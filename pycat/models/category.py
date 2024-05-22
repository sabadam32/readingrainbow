from ..extensions import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mds_number = db.Column(db.String(10), unique=True)
    mds_name = db.Column(db.String(100))
    assigned_name = db.Column(db.String(100))
    book_count = db.Column(db.Integer)
    last_updated = db.Column(db.DateTime())
