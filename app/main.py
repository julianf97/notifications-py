from fastapi import FastAPI

app = FastAPI(
    title="Notificaciones API",
    description="API para gestionar y enviar notificaciones",
    version="1.0.0",
)

@app.get("/")
def home():
    return {
        "message": "Notificaciones API funcionando"
    }

