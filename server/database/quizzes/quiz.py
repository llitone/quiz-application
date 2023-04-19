import sqlalchemy
from datetime import datetime

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
    room_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        nullable=False
    )
    start_at = sqlalchemy.Column(
        sqlalchemy.TIMESTAMP,
        default=datetime.now,
        nullable=False
    )

    def __str__(self):
        return "Quiz(id={0}, room_id={1}, start_at={2})".format(self.id, self.room_id, self.start_at)
