from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models.user import User 
from models import db

auth_bp =   Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password required'}), 400

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'error': 'Username already exist'}), 400
    
    user = User(username=username)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()
    return jsonify({message: "User created", 'username': user.username}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'error': 'Username and password required'}), 400

    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({'error':'Invalid credentials'}), 401

    token = create_access_token(identity=user.id)
    return jsonify(access_token=token), 200
    