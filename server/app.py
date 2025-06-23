from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import SQLALCHEMY_DATABASE_URI
from models import db
from flask_migrate import Migrate

from controllers.auth_controller import auth_bp
from controllers.guest_controller import guest_bp
from controllers.episode_controller import episode_bp
from controllers.appearance_controller import appearance_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['JWT_SECRET_KEY'] = 'super-secret'

db.init_app(app)
jwt = JWTManager(app)
migrate =Migrate(app, db)

app.register_blueprint(auth_bp)
app.register_blueprint(guest_bp)
app.register_blueprint(episode_bp)
app.register_blueprint(appearance_bp)

if __name__ == '__main__':
    app.run(debug=True)