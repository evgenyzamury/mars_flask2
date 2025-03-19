import flask
from flask import request, jsonify, make_response
from . import db_session
from .jobs import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return flask.jsonify(
        {
            'jobs': [item.to_dict(
                only=('id', 'job', 'team_leader', 'work_size',
                      'collaborators', 'start_date', 'is_finished')) for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:jobs_id>')
def get_one_job(jobs_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).filter(Jobs.id == jobs_id).first()
    if not jobs:
        return flask.make_response(flask.jsonify({'error': 'Bad request'}), 404)
    return flask.jsonify({'jobs':
        jobs.to_dict(only=(
            'id', 'job', 'team_leader', 'work_size', 'collaborators', 'start_date', 'is_finished'))})


@blueprint.route('/api/jobs', methods=['POST'])
def create_job():
    if not request.json:
        return flask.make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in ['job', 'team_leader', 'work_size', 'collaborators']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    job = Jobs(
        job=request.json['job'],
        team_leader=request.json['team_leader'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        start_date=request.json.get('start_date', None),
        end_date=request.json.get('end_date', None),
        is_finished=request.json.get('is_finished', False),
    )
    db_sess.add(job)
    db_sess.commit()
    return jsonify({'id': job.id})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['DELETE'])
def delete_jobs(jobs_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).filter(Jobs.id == jobs_id).first()
    if not job:
        return make_response(jsonify({'error': 'Not found'}), 404)
    db_sess.delete(job)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['PUT'])
def edit_jobs(jobs_id):
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)

    if not any([key in request.json for key in
                ['team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished']]):
        return make_response(jsonify({'error': 'Bad request'}), 400)

    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).filter(Jobs.id == jobs_id).first()
    if not jobs:
        return make_response(jsonify({'error': 'Not found'}), 400)

    new_jobs = Jobs(
        job=request.json.get('job', jobs.job),
        team_leader=request.json.get('team_leader', jobs.team_leader),
        work_size=request.json.get('work_size', jobs.work_size),
        collaborators=request.json.get('collaborators', jobs.collaborators),
        start_date=request.json.get('start_date', jobs.start_date),
        end_date=request.json.get('end_date', jobs.end_date),
        is_finished=request.json.get('is_finished', jobs.is_finished)
    )

    jobs.job = new_jobs.job
    jobs.team_leader = new_jobs.team_leader
    jobs.work_size = new_jobs.work_size
    jobs.collaborators = new_jobs.collaborators
    jobs.start_date = new_jobs.start_date
    jobs.is_finished = new_jobs.is_finished

    db_sess.commit()

    return jsonify({'success': 'ok'})
