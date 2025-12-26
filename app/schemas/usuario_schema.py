from pydantic import BaseModel
from typing import Optional


class UsuarioCreate(BaseModel):
    nombre: str
    rol: str
    estado: bool = True


class UsuarioResponse(UsuarioCreate):
    id: int
