from main import db
from flask_sqlalchemy import SQLAlchemy


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    text = db.Column(db.Text)

    def __repr__(self):
        return f'<Entry id={self.id} title={self.title}>'


def init():
    db.create_all()
