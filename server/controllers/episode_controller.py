from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models import db
from models.episode import Episode
from models.appearance import Appearance

episode_bp = Blueprint('episode_bp', __name__)

@episode_bp.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    
    return jsonify([
        {
            "id": ep.id,
            "date": ep.date.isoformat(),
            "number": ep.number
        } for ep in episodes
    ]), 200

@episode_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode_by_id(id):
    episode = Episode.query.get(id)

    if not episode:
        return jsonify({"error": "Episode not found"}), 404

    appearances = Appearance.query.filter_by(episode_id=id).all()

    return jsonify({
        "id": episode.id,
        "date": episode.date.isoformat(),
        "number": episode.number,
        "appearances": [
            {
                "id": ap.id,
                "rating": ap.rating,
                "guest_id": ap.guest_id,
                "episode_id": ap.episode_id
            } for ap in appearances
        ]
    }), 200

@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get(id)

    if not episode:
        return jsonify({"error": "Episode not found"}), 404

    db.session.delete(episode)
    db.session.commit()
    return '', 204
