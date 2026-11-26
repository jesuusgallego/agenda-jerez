from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from .config import settings
from .database import engine

app = FastAPI(title="Agenda de eventos de Jerez - API")

app.add_middleware(
    CORSMiddleware,
    allow_origins = [o.strip() for o in settings.cors_origins.split(",")],
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/health/db")
def health_db():
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    return {"db": "okme"}