from pydantic import BaseModel

##This model is used for dataValidations 
class Product(BaseModel):
    name:str
    decription:str
    price:int