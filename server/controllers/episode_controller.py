# from flask import Blueprint, jsonify
# from flask_jwt_extended import jwt_required
# from models.episode import Episode
# from models import db

# episode_bp = Blueprint('episode_bp', __name__)

# @episode_bp.route('/episode<int:id>', methods=['DELETE'])
# @jwt_required()
# def delete_episode(id):
#     episode = Episode.query.get_or_404(id)
#     db.session.delete(episode)
#     db.session.commit()
#     return jsonify(message="Episode deleted"), 200
    
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models import db
from models.episode import Episode
from models.appearance import Appearance

# Define a Blueprint for episode-related routes
episode_bp = Blueprint('episode_bp', __name__)

# GET /episodes - List all episodes
@episode_bp.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    
    # Return list of episodes
    return jsonify([
        {
            "id": ep.id,
            "date": ep.date.isoformat(),
            "number": ep.number
        } for ep in episodes
    ]), 200

# GET /episodes/<id> - Get episode details including appearances
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

# DELETE /episodes/<id> - Delete an episode (requires auth)
@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get(id)

    if not episode:
        return jsonify({"error": "Episode not found"}), 404

    db.session.delete(episode)
    db.session.commit()
    return '', 204
