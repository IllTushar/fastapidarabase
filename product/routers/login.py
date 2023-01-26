from fastapi import APIRouter,HTTPException,Depends,status
from ..import schema,model
from ..database import get_db
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import jwt,JWTError
from datetime import datetime,timedelta
pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

SECRETE_KEY="Tushar"
ALGORITHM ="HS256"
ACCES_TOKEN_EXPIER_TIME =20


router = APIRouter(
    tags=["Login"],
    prefix="/login"
)

def genrate_token(data: dict):
    to_encode= data.copy()
    expire  = datetime.utcnow() + timedelta(minutes=ACCES_TOKEN_EXPIER_TIME)
    to_encode.update({"exp":expire})
    jwt_token = jwt.encode(to_encode,SECRETE_KEY,algorithm=ALGORITHM)
    return jwt_token


@router.post("")
def login_seller(request:schema.Login,db: Session=Depends(get_db)):
    seller_login = db.query(model.Seller).filter(model.Seller.email==request.email).first()
    if not seller_login:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user email not found")
    if not pwd_context.verify(request.password,seller_login.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="invalid password")
    access_token = genrate_token(
        data={
        "sub":seller_login
    })

    return {"token":access_token}


