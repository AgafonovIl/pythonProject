from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .db_session import SqlAlchemyBase

Base = declarative_base()
metadata = Base.metadata


class Position(SqlAlchemyBase):
    __tablename__ = 'Position'

    Position_id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    oklad = Column(Integer, nullable=False)
