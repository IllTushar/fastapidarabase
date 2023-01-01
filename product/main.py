from fastapi import FastAPI,status,HTTPException
from .import schema
from .import model
from .database import engine,SessionLocal
from fastapi.params import Depends
from sqlalchemy.orm import Session
from typing import List
from passlib.context import CryptContext
app = FastAPI()

#So this line ensure that what the table define  inside the database..
model.Base.metadata.create_all(engine)
pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")
##Make Connection by using SessionLocal
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/product")
def get_all_product(db: Session=Depends(get_db)):
    products = db.query(model.Product).all()
    return products

@app.get("/product/{id}",response_model=schema.Filter_Details)
def get_specific_product(id,db: Session=Depends(get_db)):
    product = db.query(model.Product).filter(model.Product.id==id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Details not found")
    return product


@app.post('/product',status_code=status.HTTP_201_CREATED)
def add(request: schema.Product,db:Session = Depends(get_db)):
    new_product = model.Product(name=request.name,decription=request.decription,price=request.price,seller_id=1)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return request

@app.delete("/product/{id}")
def delete_data(id,db: Session=Depends(get_db)):
    Query =db.query(model.Product).filter(model.Product.id==id).delete(synchronize_session=False)
    if not Query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Product not exits")
    Query.commit()
    return {"message":"Delete Successful"}

@app.put("/product/{id}")
def update_the_table(id,request: schema.Product,db: Session = Depends(get_db)):
    product = db.query(model.Product).filter(model.Product.id==id)
    if not product.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Product not found")
    product.update(request.dict())
    db.commit()
    return {"message":"Updation Successful"}

@app.post("/seller",response_model=schema.Display,status_code=status.HTTP_201_CREATED)
def post_details(request: schema.Seller,db: Session=Depends(get_db)):
    hash_password=pwd_context.hash(request.password)
    new_seller = model.Seller(name=request.name,email=request.email,password=hash_password)
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return request
