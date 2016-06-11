from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind = engine)
session = Session()
Base = declarative_base()

class Item(Base):
    __tablename__ = 'items'
    
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)
    description = Column(String)
    start_time = Column(DateTime, default = datetime.utcnow)
    
    owner_id = Column(Integer, ForeignKey('users.id'), nullable = False)
    
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key = True)
    username = Column(String, nullable = False)
    password = Column(String, nullable = False)
    
    items = relationship("Item", uselist = False, backref="owner")
    
    
class Bid(Base):
    __tablename__ = 'bids'
    
    id = Column(Integer, primary_key = True)
    price = Column(Float, nullable = False)
    
Base.metadata.create_all(engine)

steve = User(username = 'steve', password = 'password')
george = User(username = 'george', password = 'password')
bob = User(username = 'bob', password = 'password')

baseball = Item(name = 'baseball', description = 'almost like new in box', owner = steve)

session.add_all([steve, george, bob, baseball])
session.commit()