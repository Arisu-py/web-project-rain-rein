import datetime
import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True, unique=True)
    password = sqlalchemy.Column(sqlalchemy.String, index=True, nullable=True)

    news = orm.relationship("Fan", back_populates='user')

    def __repr__(self):
        return f"<{self.__class__.__name__}> {self.id} {self.name} ({self.email})"