from pydantic import BaseModel

class ReporteIngresos(BaseModel):
    total_recaudado: float
