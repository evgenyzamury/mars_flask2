from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    id_astronaut = StringField('id астронавта', validators=[DataRequired()])
    password_astronaut = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_capitan = StringField("id капитана", validators=[DataRequired()])
    password_capitan = PasswordField("Пароль капитана", validators=[DataRequired()])
    access = SubmitField('доступ')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def index():
    return render_template('base.html', title='')


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
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/distribution')
def distribution():
    names = ['Ридли Скотт', "Эндри Уир", "Марк Уотни", "Венката Капур", "Тедди Сандрес", "Шон Бин"]
    return render_template('distribution.html', names=names)


@app.route('/table_param/<sex>/<int:age>')
def table_param(sex, age):
    return render_template('table_param.html', sex=sex, age=age)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
