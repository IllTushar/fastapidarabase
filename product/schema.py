from pydantic import BaseModel

##This model is used for dataValidations 
class Product(BaseModel):
    name:str
    decription:str
    price:int

class Filter_Details(BaseModel):
    name:str
    decription:str
    class Config:
        orm_mode=True

class Seller(BaseModel):
    name:str
    email:str
    password:str

class DisplaySeller(BaseModel):
    name :str
    email:str
    seller :Seller
    class Config:
        orm_mode =True


class Display(BaseModel):
    name:str
    email:str
    class Config:
        orm_mode = True
        


