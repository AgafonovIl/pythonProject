from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .db_session import SqlAlchemyBase

Base = declarative_base()
metadata = Base.metadata


class EmployeePosition(SqlAlchemyBase):
    __tablename__ = 'Employee_Position'

    id_Employee_Position = Column(Integer, primary_key=True,autoincrement=True)
    id_Employee = Column(ForeignKey('Employee.Employee_id'), nullable=False)
    id_Position = Column(ForeignKey('Position.Position_id'), nullable=False)

    Employee = relationship('Employee')
    Position = relationship('Position')
