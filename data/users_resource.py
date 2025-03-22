from flask_restful import abort, Api, Resource, reqparse
from flask import jsonify

from data import db_session
from data.users import User
from .reqparce_user import parser
from werkzeug.security import generate_password_hash


def set_password(password):
    return generate_password_hash(password)


def abort_if_users_not_found(user_id):
    session = db_session.create_session()
    news = session.query(User).get(user_id)
    if not news:
        abort(404, message=f"Users {user_id} not found")


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_users_not_found(user_id)
        session = db_session.create_session()
        users = session.query(User).get(user_id)
        return jsonify({'users': users.to_dict(
            only=(
                'email', 'name', 'surname', 'age', 'address', 'position', 'speciality', 'hashed_password',
            ))})

    def delete(self, user_id):
        abort_if_users_not_found(user_id)
        session = db_session.create_session()
        users = session.query(User).get(user_id)
        session.delete(users)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('email', 'name', 'surname', 'age', 'address', 'position', 'speciality', 'hashed_password',
                  )) for item in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        users = User(
            name=args['name'],
            surname=args['surname'],
            age=args['age'],
            address=args['address'],
            email=args['email'],
            position=args['position'],
            speciality=args['speciality'],
            hashed_password=set_password(args['hashed_password'])
        )
        session.add(users)
        session.commit()
        return jsonify({'id': users.id})
