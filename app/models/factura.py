# Modelo: Factura
from typing import Optional
from pydantic import BaseModel

class Factura(BaseModel):
    id: Optional[int] = None
    reserva_id: int
    subtotal: float
    impuestos: float
    total: float
