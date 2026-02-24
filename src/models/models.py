from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    weight: int | float = Field(default=None)
    exercise: bool =  Field(default=False)