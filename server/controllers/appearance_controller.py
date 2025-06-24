from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models.appearance import Appearance
from models import db

appearance_bp = Blueprint('appearance_bp', __name__)

@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()

    rating= data('rating')
    guest_id=data('guest_id')
    episode_id=data('episode_id')
    if rating is None or guest_id is None or episode_id is None:
        return jsonify({"error": "rating, guest_id, and episode_id are required"}), 400

    try:
        appearance = Appearance(rating=rating, guest_id=guest_id, episode_id=episode_id)
        db.session.add(appearance)
        db.session.commit()


        return jsonify({
            'id': appearance.id,
            'rating': appearance.rating,
            'guest_id': appearance.guest_id,
            'episode_id': appearance.episode_id
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500