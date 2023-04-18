import sqlalchemy
from sqlalchemy import orm

from ..db_session import SqlAlchemyBase

__all__ = ("Answer", )


class Answer(SqlAlchemyBase):
    __tablename__ = 'answers'

    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True,
        unique=True,
        nullable=False,
        autoincrement=True
    )
    question_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("questions.id"),
        unique=True,
        nullable=False
    )
    answer = sqlalchemy.Column(
        sqlalchemy.String,
        nullable=False
    )
    is_correct = sqlalchemy.Column(
        sqlalchemy.Boolean,
        nullable=False,
        default=False
    )
    question = orm.relationship('Question')

    def __str__(self):
        return "Answer(id={0}, question_id={1}, answer={2}, is_correct={3})".format(
            self.id, self.question_id, self.answer, self.is_correct
        )
