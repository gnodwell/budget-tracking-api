from pickle import FALSE
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy import Column, Integer, String, Float, JSON, ARRAY
from .database import Base

# Declaration of tables
class MonthylyBudget(Base): 
    __tablename__ = "monthly_budget"


    time_period = Column(String, nullable=False, primary_key=True)
    total_money = Column(String, nullable=False)
    purchase_reports = Column(JSON, nullable=True)

class MonthlyBudgetReports(Base):
    __tablename__ = "monthly_reports"

    report_id = Column(Integer, nullable=False, primary_key=True)
    time_period = Column(String, nullable=False)
    report = Column(String, nullable=True)

# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, nullable=False)
#     username = Column(String, nullable=False, unique=True)
#     password = Column(String, nullable=False, unique=True)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))