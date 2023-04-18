import sqlalchemy

from ..db_session import SqlAlchemyBase

__all__ = ("Quiz", )


class Quiz(SqlAlchemyBase):
    __tablename__ = 'quizes'

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
