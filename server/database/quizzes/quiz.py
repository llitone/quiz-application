import sqlalchemy

from ..db_session import SqlAlchemyBase

__all__ = ("Quiz", )


class Quiz(SqlAlchemyBase):
    __tablename__ = 'quizzes'

    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True,
        unique=True,
        nullable=False,
        autoincrement=True
    )
    start_at = sqlalchemy.Column(
        sqlalchemy.TIMESTAMP,
        nullable=False
    )

    def __str__(self):
        return "Quiz(id={0}, start_at={1})".format(self.id, self.start_at)
