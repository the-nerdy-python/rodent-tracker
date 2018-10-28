from flask import Blueprint, jsonify, request, render_template

from project.api.models import Rat
from project import db
from sqlalchemy import exc

rats_blueprint = Blueprint('rats', __name__, template_folder='./templates')


@rats_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        color = request.form['color']
        weight = request.form['weight']
        db.session.add(Rat(color=color, weight=weight))
        db.session.commit()
    rats = Rat.query.all()
    return render_template('index.html', rats=rats)


@rats_blueprint.route('/rats/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })


@rats_blueprint.route('/rats', methods=['POST'])
def add_rat():
    post_data = request.get_json()
    response_object = {
        'status': 'fail',
        'message': 'Invalid payload.'
    }
    if not post_data:
        return jsonify(response_object), 400
    color = post_data.get('color')
    weight = post_data.get('weight')
    try:
        db.session.add(Rat(color=color, weight=weight))
        db.session.commit()
        response_object['status'] = 'success'
        response_object['message'] = f'{color} was added!'
        return jsonify(response_object), 201
    except exc.IntegrityError as e:
        db.session.rollback()
        return jsonify(response_object), 400


@rats_blueprint.route('/rats', methods=['GET'])
def get_all_rats():
    """Get all rats"""
    response_object = {
        'status': 'success',
        'data': {
            'rats': [rat.to_json() for rat in Rat.query.all()]
        }
    }
    return jsonify(response_object), 200


@rats_blueprint.route('/rats/<rat_id>', methods=['GET'])
def get_single_rat(rat_id):
    """Get single rat details"""
    response_object = {
        'status': 'fail',
        'message': 'Rat does not exist'
    }
    try:
        rat = Rat.query.filter_by(id=int(rat_id)).first()
        if not rat:
            return jsonify(response_object), 404
        else:
            response_object = {
                'status': 'success',
                'data': {
                    'id': rat.id,
                    'color': rat.color,
                    'weight': rat.weight,
                    'active': rat.active
                }
            }
            return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404
