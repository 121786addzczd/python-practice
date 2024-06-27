from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


# パスパラメータ
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
#  http://127.0.0.1:8000/items/foo


# クエリパラメータ
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
# http://127.0.0.1:8000/items/?skip=0&limit=10


# リクエストボデイ
@app.post("/items/")
async def create_item(item: Item):
    return item