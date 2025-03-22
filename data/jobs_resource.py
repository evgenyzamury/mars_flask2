from flask_restful import abort, Resource
from flask import jsonify

from data import db_session
from data.jobs import Jobs
from .reqparce_jobs import parser, put_parser


def abort_if_jobs_not_found(jobs_id):
    session = db_session.create_session()
    jobs = session.query(Jobs).get(jobs_id)
    if not jobs:
        abort(404, message=f"jobs {jobs_id} not found")


class JobsResource(Resource):
    def get(self, jobs_id):
        abort_if_jobs_not_found(jobs_id)
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == jobs_id).first()
        return jsonify({'jobs': jobs.to_dict(
            only=('job', 'team_leader', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished'))})

    def delete(self, jobs_id):
        abort_if_jobs_not_found(jobs_id)
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == jobs_id).first()
        db_sess.delete(jobs)
        db_sess.commit()
        return jsonify({'success': 'OK'})

    def put(self, jobs_id):
        args = put_parser.parse_args()
        none = [i for i in args if args[i] is None]  # находим пустые значения словаря
        for i in none:
            args.pop(i)  # удаляем элементы с пустыми ключами

        abort_if_jobs_not_found(jobs_id)
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == jobs_id).first()
        new_jobs = Jobs(
            team_leader=args.get('team_leader', jobs.team_leader),
            job=args.get('job', jobs.job),
            work_size=args.get('work_size', jobs.work_size),
            collaborators=args.get('collaborators', jobs.collaborators),
            start_date=args.get('start_date', jobs.start_date),
            end_date=args.get('end_date', jobs.end_date),
            is_finished=args.get('is_finished', jobs.is_finished)
        )

        jobs.job = new_jobs.job
        jobs.team_leader = new_jobs.team_leader
        jobs.work_size = new_jobs.work_size
        jobs.collaborators = new_jobs.collaborators
        jobs.start_date = new_jobs.start_date
        jobs.end_date = new_jobs.end_date
        jobs.is_finished = new_jobs.is_finished

        db_sess.commit()
        return jsonify({'OK': 'success'})


class JobsResourceList(Resource):
    def get(self):
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).all()
        return jsonify({'jobs': [item.to_dict(
            only=('job', 'team_leader', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished')) for item
            in jobs]})

    def post(self):
        args = parser.parse_args()
        db_sess = db_session.create_session()
        jobs = Jobs(
            team_leader=args['team_leader'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            start_date=args.get('start_date', None),
            end_date=args.get('end_date', None),
            is_finished=args.get('is_finished', False)
        )
        db_sess.add(jobs)
        db_sess.commit()
        return jsonify({'id': jobs.id})
