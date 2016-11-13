from sqlalchemy import Column, Integer, String
from sqlalchemy.types import ARRAY
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Tweet(Base):
	__tablename__ = 'tweet'
	id = Column(Integer, primary_key=True)
	user = Column(String)
	text = Column(String)
	hashtags = Column(ARRAY(String))