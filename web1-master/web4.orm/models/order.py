from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .db_session import SqlAlchemyBase


class Order(SqlAlchemyBase):
    __tablename__ = 'Order'

    Order_id = Column(Integer, primary_key=True,autoincrement=True)
    price = Column(Integer, nullable=False)
    title = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
