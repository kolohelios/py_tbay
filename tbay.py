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
    bids = relationship("Bid", backref = 'item')
    
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key = True)
    username = Column(String, nullable = False)
    password = Column(String, nullable = False)
    
    items = relationship("Item", uselist = False, backref = "owner")
    bids = relationship("Bid", backref = 'bidder')
    
class Bid(Base):
    __tablename__ = 'bids'
    
    id = Column(Integer, primary_key = True)
    price = Column(Float, nullable = False)
    
    item_id = Column(Integer, ForeignKey('items.id'), nullable = False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable = False)
    
Base.metadata.create_all(engine)

steve = User(username = 'Steve', password = 'password')
george = User(username = 'George', password = 'password')
bob = User(username = 'Bob', password = 'password')

baseball = Item(name = 'baseball', description = 'almost like new in box', owner = steve)

bid = Bid(price = 9.99, item = baseball, bidder = george)
bid2 = Bid(price = 10.99, item = baseball, bidder = bob)
bid3 = Bid(price = 11.99, item = baseball, bidder = george)
session.add_all([steve, george, bob, baseball, bid, bid2, bid3])
session.commit()

winning_bid = session.query(Bid).filter(Item.name == 'baseball').order_by(Bid.price.desc()).first()
print(winning_bid.bidder.username, 'won the auction for the', winning_bid.item.name, 'with a bid of ${}'.format(winning_bid.price))
