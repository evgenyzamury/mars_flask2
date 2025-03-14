import datetime
import os

from flask import Flask, render_template, redirect, request, json
from flask_login import LoginManager, login_user, login_required, current_user

from data import db_session
from data.jobs import Jobs
from data.users import User
from forms.login import LoginForm
from forms.user import RegisterForm
from forms.jobs import JobsForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).join(User, User.id == Jobs.team_leader).all()
    from_id_to_name = dict()
    for item in jobs:
        user = db_sess.query(User).filter(User.id == item.team_leader).first()
        from_id_to_name[item.team_leader] = f'{user.name} {user.surname}'
    return render_template('workslog.html', jobs=jobs, from_id_to_name=from_id_to_name)


@app.route('/<title>')
@app.route('/index/<title>')
def index_title(title):
    return render_template('base.html', title=title)


@app.route('/training/<name>')
def training(name):
    return render_template('training.html', prof=name.lower())


@app.route('/list_prof/<lst>')
def list_prof(lst):
    professions = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', "врач", "инженер по терраформированию",
                   "климатолог"]
    return render_template('list_prof.html', lst=lst, professions=professions)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    params = {
        "title": "Анкета",
        "surname": "Watny",
        "name": "Mark",
        "education": "выше среднего",
        "proffesion": "штурман марсахода",
        "sex": "male",
        "motivation": "Всегда мечтал застрять на Марсе!",
        "ready": 'True'
    }
    return render_template('auto_answer.html', **params)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/news', methods=['GET', 'POST'])
@login_required
def add_news():
    form = JobsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        jobs = Jobs()
        jobs.job = form.job.data
        jobs.team_leader = form.job.data
        jobs.work_size = form.job.data
        jobs.collaborators = form.collaborators.data
        current_user.jobs.append(jobs)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/')
    return render_template('jobs.html', title='Добавление новости',
                           form=form)
@app.route('/distribution')
def distribution():
    names = ['Ридли Скотт', "Эндри Уир", "Марк Уотни", "Венката Капур", "Тедди Сандрес", "Шон Бин"]
    return render_template('distribution.html', names=names)


@app.route('/table_param/<sex>/<int:age>')
def table_param(sex, age):
    return render_template('table_param.html', sex=sex, age=age)


@app.route('/carousel', methods=['POST', 'GET'])
def carousel():
    if request.method == 'POST':
        images = os.listdir('static/img/carousel')
        file_number = images[-1][13:images[-1].find('.'):]
        file_number = f"{int(file_number) + 1}"
        with open('static/img/carousel/mars_carousel' + file_number + '.png', 'wb') as file:
            file.write(request.files['file'].read())
        images.append('mars_carousel' + file_number + '.png')
        request.method = 'GET'
    else:
        images = os.listdir('static/img/carousel')
    return render_template('carousel.html', images=images)


@app.route("/member")
def member():
    with open('templates/members_info.json', 'rt', encoding='UTF-8') as file:
        members_json = json.loads(file.read())
    return render_template('member.html', members_json=members_json)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.repeat_password.data:
            return render_template('register.html', title='регистрация', form=form, message='пароли не совпадают')
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='регистрация', form=form,
                                   message='такой пользователь уже есть')
        user = User(
            email=form.email.data,
            surname=form.surname.data,
            name=form.name.data,
            age=int(form.age.data),
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
            modified_date=datetime.datetime.now()
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/')
    return render_template('register.html', title='Регистрация', form=form)


if __name__ == '__main__':
    db_session.global_init('db/blogs.db')
    db_sess = db_session.create_session()
    if not bool(db_sess.query(User).first()):  # создаём пример из задания если бд пустая
        # users
        # user 1
        user = User()
        user.surname = 'Scott'
        user.name = 'Ridley'
        user.age = 21
        user.position = 'capatain'
        user.speciality = 'research engineer'
        user.address = 'module_1'
        user.email = 'scott_chief@mars.org'
        db_sess.add(user)
        db_sess.commit()
        # user 2
        user = User()
        user.surname = 'Dray'
        user.name = 'Megel'
        user.age = 25
        user.position = 'technic'
        user.speciality = 'geniy'
        user.address = 'module_2'
        user.email = 'dray_meg@mars.org'
        db_sess.add(user)
        db_sess.commit()
        # user 3
        user = User()
        user.surname = 'Romal'
        user.name = 'Maks'
        user.age = 25
        user.position = 'driver'
        user.speciality = 'hard driver'
        user.address = 'module_3'
        user.email = 'roma_maks@mars.org'
        db_sess.add(user)
        db_sess.commit()
        # user 4
        user = User()
        user.surname = 'Muriy'
        user.name = 'Tom'
        user.age = 24
        user.position = 'builder'
        user.speciality = 'expert'
        user.address = 'module_4'
        user.email = 'tom_mur@mars.org'
        db_sess.add(user)
        db_sess.commit()
        # jobs
        # job 1
        job = Jobs()
        job.team_leader = 1
        job.job = 'deployment of residential modules 1 and 2'
        job.work_size = 15
        job.start_date = datetime.datetime.now()
        job.is_finished = False
        db_sess.add(job)
        db_sess.commit()
        # job 2
        job = Jobs()
        job.team_leader = 4
        job.job = 'build sceleton tower'
        job.work_size = 20
        job.start_date = datetime.datetime.now()
        job.is_finished = False
        db_sess.add(job)
        db_sess.commit()

    app.run(port=8080, host='127.0.0.1')
