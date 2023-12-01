# Referencia: https://fastapi.tiangolo.com/tutorial/sql-databases/#create-the-database-models

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
  __tablename__ = "users"
  __table_args__ = {'extend_existing': True}

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, nullable=False)
  connection = Column(String, nullable=True)
  role = Column(String, default="USER")
  email = Column(String, unique=True, index=True, nullable=False)
  password = Column(String, nullable=True)
  is_active = Column(Boolean, default=True)
  activation_code = Column(Integer, nullable=True)
  password_reset_code = Column(Integer, nullable=True)


  social_users = relationship("SocialUser", back_populates="user")

class SocialUser(Base):
    __tablename__ = "social_users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    role = Column(String, default="USER")

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="social_users")

