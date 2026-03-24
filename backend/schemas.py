from pydantic import BaseModel,ConfigDict
from datetime import datetime
from typing import Optional

#  validar los datos que llegan por la API 
# antes de tocar la base de datos con Pydantic.


class TicketCreate(BaseModel):
    titulo:str
    descripcion:str
    prioridad:str 

class TicketUpdate(BaseModel):
    categoria:Optional[str]  

class TicketResponse(BaseModel):
    id:int
    titulo:str
    descripcion:str
    prioridad:str 
    categoria:Optional[str] 
    estado:str
    fecha_creacion:datetime

    model_config = ConfigDict(from_attributes=True) # porque en Pydantic v2 la configuración de los modelos ya no se hace con una clase interna Config

