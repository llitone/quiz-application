import sqlalchemy

from ..db_session import SqlAlchemyBase

__all__ = ("AppUser",)


class AppUser(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True,
        unique=True,
        nullable=False,
        autoincrement=True
    )
    name = sqlalchemy.Column(
        sqlalchemy.String,
        nullable=False
    )
    age = sqlalchemy.Column(
        sqlalchemy.Integer,
        nullable=False
    )
    phone_number = sqlalchemy.Column(
        sqlalchemy.String,
        nullable=False,
        unique=True
    )
    password = sqlalchemy.Column(
        sqlalchemy.String,
        nullable=False
    )
    points = sqlalchemy.Column(
        sqlalchemy.Integer,
        nullable=False
    )

    def __str__(self):
        return "User(id={0}, name={1}, phone_number={2}, password={3})".format(
            self.id, self.name, self.phone_number, self.password
        )

    def json(self=None):  # pep8 fix for .first().json()
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "phone_number": self.phone_number,
            "password": self.password,
            "points": self.points
        }
