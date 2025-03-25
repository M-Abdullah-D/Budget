from sqlalchemy import Column, Integer, String, Float
from database import Base

class Budget(Base):
    __tablename__ = "budget"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, index=True)  # "Assets", "Investments", "Costs"
    amount = Column(Float, nullable=False)
    currency = Column(String, default="USD")
