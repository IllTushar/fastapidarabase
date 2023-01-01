from sqlalchemy import Column,Integer,String,ForeignKey
from .database import Base
from sqlalchemy.orm import relationship
## This model is used to create the table inside the database....

##This model is the blueprint to create the database in the backend so that you 
##don't have to write any kind of sequel
class Product(Base):
    __tablename__='products'
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    decription = Column(String)
    price =Column(Integer)
    seller_id = Column(Integer,ForeignKey('sellers.id'))
    seller = relationship("Seller",back_populates='products')

class Seller(Base):
    __tablename__ = 'sellers'
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    email = Column(String)
    password= Column(String)
    products = relationship("Product",back_populates='seller')


