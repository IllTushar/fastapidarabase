from fastapi import FastAPI
from .import model
from .database import engine
from .routers import product_user,seller,login
app = FastAPI(
    title="ProductAPI's",
    description="All the API's are connected with product app",
    terms_of_service="http://google.com",
    contact={
        "name":"Tushar Gupta",
        "email": "gtushar@gamil.com"
    },
)
app.include_router(product_user.router)
app.include_router(seller.router)
app.include_router(login.router)
#So this line ensure that what the table define  inside the database..
model.Base.metadata.create_all(engine)





