from flask import Flask, render_template

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
