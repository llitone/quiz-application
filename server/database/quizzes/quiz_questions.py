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

    def __str__(self):
        return "QuizQuestion(id={0}, quiz_id={1}, question_id={2}, is_correct={3})".format(
            self.id, self.quiz_id, self.question_id, self.is_correct
        )
