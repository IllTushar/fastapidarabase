from fastapi import FastAPI,Query,Depends
from pydantic import BaseModel
from typing import Optional,List
# from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# from database import Base,engine,SessionLocal

# class User(Base):
#     __tablename__="users"
#     id = Column(Integer,primary_key=True,index=True)
#     email = Column(String,unique=True,index=True)
#     is_active = Column(Boolean,default=True)

# Base.metadata.create_all(bind=engine)
app = FastAPI()


