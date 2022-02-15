from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .db_session import SqlAlchemyBase


class EmployeeOrder(SqlAlchemyBase):
    __tablename__ = 'Employee_Order'

    id_Employee_Order = Column(Integer, primary_key=True, autoincrement=True)
    id_Employee = Column(ForeignKey('Employee.Employee_id'), nullable=False)
    id_Order = Column(ForeignKey('Order.Order_id'), nullable=False)

    Employee = relationship('Employee')
    Order = relationship('Order')
