from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .db_session import SqlAlchemyBase


class Client(SqlAlchemyBase):
    __tablename__ = 'Client'

    Client_id = Column(Integer, primary_key=True,autoincrement=True)
    full_name = Column(Text, nullable=False)
    phone = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
