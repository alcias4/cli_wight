from sqlmodel import SQLModel, create_engine

DATABASE_URL = "sqlite:///database.db"
engine = create_engine(DATABASE_URL)

def create_db() -> None:
    import models.models
    SQLModel.metadata.create_all(engine)