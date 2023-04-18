import sqlalchemy
from sqlalchemy import orm

from ..db_session import SqlAlchemyBase

__all__ = ("Question", )


class Question(SqlAlchemyBase):
    __tablename__ = 'questions'

    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True,
        unique=True,
        nullable=False,
        autoincrement=True
    )
    age = sqlalchemy.Column(
        sqlalchemy.Integer,
        nullable=False
    )
    question = sqlalchemy.Column(
        sqlalchemy.String,
        nullable=False
    )
    difficulty = sqlalchemy.Column(
        sqlalchemy.Integer,
        nullable=False
    )
    value = sqlalchemy.Column(
        sqlalchemy.Integer,
        nullable=False
    )
    subject_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("subjects.id")
    )
    subject = orm.relationship('Subject')
