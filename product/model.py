from sqlalchemy import Column,Integer,String
from .database import Base
## This model is used to create the table inside the database....

##This model is the blueprint to create the database in the backend so that you 
##don't have to write any kind of sequel
class Product(Base):
    __tablename__='products'
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    decription = Column(String)
    price =Column(Integer)


