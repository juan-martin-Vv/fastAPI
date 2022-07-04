
from typing import Union
from fastapi import FastAPI
from models import *
from database import inicia, insertDB, leerDBall, leerDBlast


app = FastAPI()
inicia()
triger = commit(comit="",hasid="")
@app.post("/comit")
def push_comit(data:commit):
    global triger
    triger = data
    insertDB(data.comit,data.hasid)
    return "se ha detectado un commit"

@app.get("/")
def read_root():
    data:commit
    data=leerDBlast()
    print(data)
    # return data
    return "se ralizado un commit en "+data.comit+" con el ID :"+data.hasid

@app.get("/all")
def read_root():
    data:commit
    data=leerDBlast()
    return data

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/")
def leer(data:cuerpo):
    data.nombre=data.nombre.upper()
    return data