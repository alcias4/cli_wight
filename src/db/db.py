from sqlmodel import SQLModel, create_engine
import os
from dotenv import load_dotenv

load_dotenv () # Cargar v entorno
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("No se encontró DATABASE_URL en el .env")

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, connect_args=connect_args)

def create_db() -> None:
    import models.models
    SQLModel.metadata.create_all(engine)