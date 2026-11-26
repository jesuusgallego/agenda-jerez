from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_FILE = Path(__file__).resolve().parents[2] / ".env"

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file = ENV_FILE, extra = "ignore")

    database_url: str
    app_name: str = "Agenda de eventos de Jerez"

    cors_origins: str = "http://localhost:5173"

settings = Settings()