from pydantic import BaseModel

class HabitacionCreate(BaseModel):
    numero: str
    tipo: str
    precio: float
    disponible: bool = True

class HabitacionResponse(HabitacionCreate):
    id: int
