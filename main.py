from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

class cuerpo(BaseModel):
    nombre:str
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/")
def leer(data:cuerpo):
    data.nombre=data.nombre.upper()
    return data
if __name__ == "__main__":
    uvicorn.run("example:app", host="127.0.0.1", port=5000, log_level="info")