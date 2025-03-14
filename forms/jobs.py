from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    job = StringField('Название', validators=[DataRequired()])
    team_leader = IntegerField("id руководителя", validators=[DataRequired()])
    work_size = IntegerField("Объём работ", validators=[DataRequired()])
    collaborators = StringField('Исполнители', validators=[DataRequired()])
    is_finished = BooleanField('Работа выполнена')
    submit = SubmitField('Создать')
