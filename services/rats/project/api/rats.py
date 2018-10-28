from flask import Blueprint, jsonify


rats_blueprint = Blueprint('rats', __name__)


@rats_blueprint.route('/rats/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })