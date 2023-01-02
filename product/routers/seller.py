from fastapi import APIRouter,HTTPException,status
from ..import model,schema
from fastapi.params import Depends
from sqlalchemy.orm import Session
from ..database import get_db
from passlib.context import CryptContext

router =APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")
@router.post("/seller",response_model=schema.Display,status_code=status.HTTP_201_CREATED,tags=["Seller_Details"])
def post_details(request: schema.Seller,db: Session=Depends(get_db)):
    hash_password=pwd_context.hash(request.password)
    new_seller = model.Seller(name=request.name,email=request.email,password=hash_password)
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return request

