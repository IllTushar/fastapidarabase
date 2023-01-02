##Create an engine.....
from sqlalchemy import create_engine,engine
##Connect the database....
from sqlalchemy.ext.declarative import declarative_base
##Connect the session....
from sqlalchemy.orm import sessionmaker 

SQLALCHEMY_DATABASE_URL = "sqlite:///./product.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={
    "check_same_thread":False
})
SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)
Base = declarative_base()


##Make Connection by using SessionLocal
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()