import datetime

import flask
from flask import make_response, jsonify, request
from . import db_session
from .users import User

blueprint = flask.Blueprint('user_api', __name__, template_folder='templates')


@blueprint.route('/api/users')
def get_users():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return jsonify({'Users': [item.to_dict(
        only=('id', 'surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'modified_date')) for item
        in users]})


@blueprint.route('/api/users/<int:user_id>')
def get_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == user_id).first()
    if not user:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify({'User': user.to_dict(
        only=('id', 'surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'modified_date'))})


@blueprint.route('/api/users', methods=['POST'])
def add_users():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)

    if not all([key in request.json for key in
                ['surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'password']]):
        return make_response(jsonify({'error': 'Bad request'}), 400)

    db_sess = db_session.create_session()

    user = User(
        surname=request.json['surname'],
        name=request.json['name'],
        age=request.json['age'],
        position=request.json['position'],
        speciality=request.json['speciality'],
        address=request.json['address'],
        email=request.json['email'],
    )
    user.set_password(request.json['password'])

    db_sess.add(user)
    db_sess.commit()

    return jsonify({'id': user.id})


@blueprint.route('/api/users/<int:user_id>', methods=['PUT'])
def edit_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == user_id).first()

    if not user:
        return make_response(jsonify({'error': 'Not found'}), 404)

    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)

    if not any([key in request.json for key in
                ['surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'password']]):
        return make_response(jsonify({'error': 'Bad request'}), 400)

    new_user = User(
        surname=request.json.get('surname', user.surname),
        name=request.json.get('name', user.name),
        age=request.json.get('age', user.age),
        position=request.json.get('position', user.position),
        speciality=request.json.get('speciality', user.speciality),
        address=request.json.get('address', user.address),
        email=request.json.get('email', user.email),
        hashed_password=user.hashed_password,
    )

    if 'password' in request.json:
        new_user.set_password(request.json['password'])

    user.surname = new_user.surname
    user.name = new_user.name
    user.age = new_user.age
    user.position = new_user.position
    user.speciality = new_user.speciality
    user.address = new_user.address
    user.email = new_user.email
    user.modified_date = datetime.datetime.now()
    user.hashed_password = new_user.hashed_password

    db_sess.commit()

    return make_response(jsonify({'success': 'OK'}))


@blueprint.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == user_id).first()
    if not user:
        return make_response(jsonify({'error': 'Not found'}), 404)
    db_sess.delete(user)
    db_sess.commit()
    return jsonify({'success': 'ok'})

