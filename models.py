from typing_extensions import Self
from pydantic import BaseModel
class cuerpo(BaseModel):
    nombre:str

class commit(BaseModel):
    comit:str
    hasid:str
    def seter(comiti:str,hasidi:str):
        Self.comit=comiti
        Self.hasid=hasidi
