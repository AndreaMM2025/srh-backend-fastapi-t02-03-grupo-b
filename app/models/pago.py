# Modelo: Pago
from typing import Optional
from pydantic import BaseModel

class Pago(BaseModel):
    id: Optional[int] = None
    factura_id: int
    fecha: str
    monto: float
    metodo: str
