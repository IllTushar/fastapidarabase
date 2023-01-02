
from fastapi import APIRouter,HTTPException,status
from fastapi.params import Depends
from sqlalchemy.orm import Session
from   ..import model,schema
from typing import List
from ..database import get_db
router = APIRouter()




@router.get("/product",tags=["GET PRODUCT"])
def get_all_product(db: Session=Depends(get_db)):
    products = db.query(model.Product).all()
    return products

@router.get("/product/{id}",response_model=schema.Filter_Details,tags=["GET SPECIFIC PRODUCT"])
def get_specific_product(id,db: Session=Depends(get_db)):
    product = db.query(model.Product).filter(model.Product.id==id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Details not found")
    return product


@router.post('/product',status_code=status.HTTP_201_CREATED,tags=["POST THE DATA"])
def add(request: schema.Product,db:Session = Depends(get_db)):
    new_product = model.Product(name=request.name,decription=request.decription,price=request.price,seller_id=1)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return request

@router.delete("/product/{id}",tags=["DELETE THE DATA"])
def delete_data(id,db: Session=Depends(get_db)):
    Query =db.query(model.Product).filter(model.Product.id==id).delete(synchronize_session=False)
    if not Query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Product not exits")
    db.commit()
    return {"message":"Delete Successful"}

@router.put("/product/{id}",tags=["UPDATE THE DATA"])
def update_the_table(id,request: schema.Product,db: Session = Depends(get_db)):
    product = db.query(model.Product).filter(model.Product.id==id)
    if not product.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Product not found")
    product.update(request.dict())
    db.commit()
    return {"message":"Updation Successful"}