from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('name', required=True)
parser.add_argument('surname', required=True)
parser.add_argument('email', required=True)
parser.add_argument('age', type=int, required=True)
parser.add_argument('position', required=True)
parser.add_argument('speciality', required=True)
parser.add_argument('address', required=True)
parser.add_argument('hashed_password', required=True)


put_parser = reqparse.RequestParser()
put_parser.add_argument('name')
put_parser.add_argument('surname')
put_parser.add_argument('email')
put_parser.add_argument('age', type=int)
put_parser.add_argument('position')
put_parser.add_argument('speciality')
put_parser.add_argument('address')
put_parser.add_argument('hashed_password')
