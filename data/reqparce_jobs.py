import datetime

from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('job', required=True)
parser.add_argument('team_leader', required=True, type=int)
parser.add_argument('work_size', type=int, required=True)
parser.add_argument('collaborators', required=True)
parser.add_argument('start_date', type=datetime.datetime)
parser.add_argument('end_date', type=datetime.datetime)
parser.add_argument('is_finished', type=bool)


put_parser = reqparse.RequestParser()
put_parser.add_argument('job')
put_parser.add_argument('team_leader', type=int)
put_parser.add_argument('work_size', type=int)
put_parser.add_argument('collaborators')
put_parser.add_argument('start_date', type=datetime.datetime)
put_parser.add_argument('end_date', type=datetime.datetime)
put_parser.add_argument('is_finished', type=bool)
