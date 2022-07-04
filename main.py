from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

class cuerpo(BaseModel):
    nombre:str

class commit(BaseModel):
    comit:str
    hasid:str

app = FastAPI()
triger = commit
@app.post("/comit")
def push_comit(data:commit):
    triger=data
    return "se ralizado un commit en "+data.comit+" con el ID :"+data.hasid

@app.get("/")
def read_root():
    return "se ralizado un commit en "+triger.comit+" con el ID :"+triger.hasid


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/")
def leer(data:cuerpo):
    data.nombre=data.nombre.upper()
    return data