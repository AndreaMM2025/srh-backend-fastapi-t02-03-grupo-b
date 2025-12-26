# Modelo: Usuario
from typing import Optional
from pydantic import BaseModel

class Usuario(BaseModel):
    id: Optional[int] = None
    nombre: str
    rol: str
    estado: bool = True
