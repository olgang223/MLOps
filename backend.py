from typing import Union

from fastapi import FastAPI

app = FastAPI()

def scoring(item_id: int, q: int):
    return item_id * q

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def reader(item_id: int, q: int):
    return {"item id": item_id, "quantity": q}

@app.get("/score/{item_id}")
def score(item_id: int, q: int):
    s = scoring(item_id, q)
    return {"item id": item_id, "quantity": q, "score":s}