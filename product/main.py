from fastapi import FastAPI
from .import schema
from .import model
from .database import engine,SessionLocal
from fastapi.params import Depends
from sqlalchemy.orm import Session
app = FastAPI()

#So this line ensure that what the table define  inside the database..
model.Base.metadata.create_all(engine)

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

@app.get("/product/{id}")
def get_specific_product(id,db: Session=Depends(get_db)):
    product = db.query(model.Product).filter(model.Product.id==id).first()
    return product


@app.post('/product')
def add(request: schema.Product,db:Session = Depends(get_db)):
    new_product = model.Product(name=request.name,decription=request.decription,price=request.price)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return request

@app.delete("/product/{id}")
def delete_data(id,db: Session=Depends(get_db)):
    db.query(model.Product).filter(model.Product.id==id).delete(synchronize_session=False)
    db.commit()
    return {"message":"Delete Successful"}

@app.put("/product/{id}")
def update_the_table(id,request: schema.Product,db: Session = Depends(get_db)):
    product = db.query(model.Product).filter(model.Product.id==id)
    if not product.first():
        # return {"message":"user not exists"}
        pass
    product.update(request.dict())
    db.commit()
    return {"message":"Updation Successful"}


