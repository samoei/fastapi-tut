from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Martians"}


@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.get("/users/me")
async def get_current_user():
    return {"id": 1, "name": "Phil Samoei", "role": "admin"}


@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"id": user_id, "name": "John Doe", "role": "basic"}
