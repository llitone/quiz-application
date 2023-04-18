import sqlalchemy
from sqlalchemy import orm

from ..db_session import SqlAlchemyBase

__all__ = ("QuizQuestion", )


class QuizQuestion(SqlAlchemyBase):
    __tablename__ = 'quiz_question'

    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True,
        unique=True,
        nullable=False,
        autoincrement=True
    )
    quiz_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("quizzes.id")
    )
    question_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("questions.id")
    )
    is_correct = sqlalchemy.Column(
        sqlalchemy.Boolean,
        nullable=False,
        default=False
    )
    quiz = orm.relationship("Quiz")
