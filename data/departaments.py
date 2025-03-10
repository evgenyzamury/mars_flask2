from .db_session import SqlAlchemyBase
from sqlalchemy import orm
import sqlalchemy


class Departament(SqlAlchemyBase):
    __tablename__ = 'departaments'
    id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'), autoincrement=True, primary_key=True)
    title = sqlalchemy.Column(sqlalchemy.String)
    chief = sqlalchemy.Column(sqlalchemy.Integer)
    members = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=False)
    user = orm.relationship('User')
