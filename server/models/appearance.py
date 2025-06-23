from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from models import db

class Appearance(db.Model):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey("episodes.id"), nullable=False)

    @validates('rating')
    def validate_rating(self, key, value):
        if value < 1 or value > 5:
            raise ValueError("Rating must be between 1 and 5")
        return value

    def __repr__(self):
        return f"<Appearance Guest ID {self.guest_id}, Episode ID {self.episode_id}, Rating {self.rating}>"