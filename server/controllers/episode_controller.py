from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from models.episode import Episode
from models import db

episode_bp = Blueprint('episode_bp', __name__)

@episode_bp.route('/episode<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify(message="Episode deleted"), 200