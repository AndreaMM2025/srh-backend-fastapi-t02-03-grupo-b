from fastapi import FastAPI
from app.routers import clientes

app = FastAPI(title="SRH Backend")

@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}

app.include_router(clientes.router)
# para visualizar la pagina del srh backend http://127.0.0.1:8000/docsv