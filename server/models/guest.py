# from flask_sqlalchemy import SQLAlchemy
from models import db
# db = SQLAlchemy()

class Guest(db.Model):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    occupation = db.Column(db.String)

    def __repr__(self):
        return f"<Guest {self.name}, {self.occupation}>"