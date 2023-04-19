import sqlalchemy

from ..db_session import SqlAlchemyBase

__all__ = ("Author",)


class Author(SqlAlchemyBase):
    __tablename__ = 'authors'

    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True,
        unique=True,
        nullable=False,
        autoincrement=True
    )
    login = sqlalchemy.Column(
        sqlalchemy.String,
        nullable=False,
        unique=True
    )
    password = sqlalchemy.Column(
        sqlalchemy.String,
        nullable=False
    )
