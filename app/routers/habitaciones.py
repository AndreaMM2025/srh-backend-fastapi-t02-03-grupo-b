from fastapi import APIRouter
from app.schemas.habitacion_schema import HabitacionCreate, HabitacionResponse

router = APIRouter(
    prefix="/api/habitaciones",
    tags=["Habitaciones"]
)

# Base de datos en memoria
habitaciones_db: list[dict] = []

@router.get("/", response_model=list[HabitacionResponse])
def listar_habitaciones():
    return habitaciones_db

@router.post("/", response_model=HabitacionResponse)
def crear_habitacion(habitacion: HabitacionCreate):
    nueva = {
        "id": len(habitaciones_db) + 1,
        **habitacion.model_dump()
    }
    habitaciones_db.append(nueva)
    return nueva
