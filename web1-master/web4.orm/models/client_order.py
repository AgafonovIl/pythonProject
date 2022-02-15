from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .db_session import SqlAlchemyBase


class ClientOrder(SqlAlchemyBase):
    __tablename__ = 'Client_Order'

    id_Client_Order = Column(Integer, primary_key=True,autoincrement=True)
    id_Order = Column(ForeignKey('Order.Order_id'), nullable=False)
    id_Client = Column(ForeignKey('Client.Client_id'), nullable=False)

    Client = relationship('Client')
    Order = relationship('Order')
