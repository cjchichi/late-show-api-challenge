from app import app
from models import db
from models.user import User
from models.guest import Guest
from models.episode import Episode
from models.appearance import Appearance

from datetime import date

with app.app_context():
    print("Seeding data")

    Appearance.query.delete()
    Guest.query.delete()
    Episode.query.delete()
    User.query.delete()

    user = User(username='admin')
    user.set_password('password123')
    db.session.add(user)

    
    g1 = Guest(name="Zendaya", occupation="Actress")
    g2 = Guest(name="Trevor Noah", occupation="Comedian")
    db.session.add_all([g1, g2])

    
    e1 = Episode(date=date(2025, 6, 1), number=1)
    e2 = Episode(date=date(2025, 6, 2), number=2)
    db.session.add_all([e1, e2])

    a1 = Appearance(rating=5, guest_id=1, episode_id=1)
    a2 = Appearance(rating=4, guest_id=2, episode_id=2)
    db.session.add_all([a1, a2])

    db.session.commit()
    print("Done seeding!")