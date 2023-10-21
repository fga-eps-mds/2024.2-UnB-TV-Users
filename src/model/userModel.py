# Referencia: https://fastapi.tiangolo.com/tutorial/sql-databases/#create-the-database-models

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, index=True)
  email = Column(String, unique=True, index=True)
  password = Column(String)
  is_active = Column(Boolean, default=True)