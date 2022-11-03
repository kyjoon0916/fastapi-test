from typing import Union, Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Token(BaseModel):
    text: str


@app.get("/")
def read_root():
    return {"Hello": "World12312312231233456456"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/check_name/")
def get_name(text: Token):
    return {"name": name_tag(text.text)}
