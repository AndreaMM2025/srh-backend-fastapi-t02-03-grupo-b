from fastapi import FastAPI

app = FastAPI(title="SRH Backend")

@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}
