# Object for total set budget per month
# Determine ways to decrease from value
# Track decrements
# create categories for expenses
# creates categorie customization

# from fastapi import FastAPI
from fastapi import FastAPI
import models

from objects.balance import Balance
from schemas import ValueQuery
from database import engine


models.Base.metadata.create_all(bind=engine)


app = FastAPI()

balance = Balance(4000)


@app.get("/")
def root():
    return {"data": "Hello World"}


@app.get("/get-balance")
def getBalance():
    return {"data": balance.getBlanace()}

@app.post("/decrease-balance")
def decreaseBalance(valueQuery: ValueQuery):
    if (valueQuery != None):
        balance.decreaseBalance(valueQuery.value)
        print(valueQuery.note)
    
    return {"data": balance.getBlanace()}

@app.post("/increase-balance")
def increaseBalance(valueQuery: ValueQuery):
    if (valueQuery != None):
        balance.increaseBalance(valueQuery.value)
        print(valueQuery.note)
    
    return {"data": balance.getBlanace()}