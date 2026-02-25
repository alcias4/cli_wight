from sqlmodel import create_engine, Session, select
from db.db import DATABASE_URL
from models.models import User
from typing import Sequence


engine = create_engine(DATABASE_URL)

def insert_register(weight: float, exercise: bool):
    with Session(engine) as session:
        register = User(exercise=exercise, weight=weight)
        session.add(register)
        session.commit()
        session.refresh(register)

        print("insert: ", register)


def update_register(id: int, weight:float, exercise:bool ):
    with Session(engine) as session:
        register = session.get(User, id)

        if register is None:
            print("No found id or register")
            return


        if weight != None:
            register.weight = weight
        
        if exercise != None:
            register.exercise = exercise

        session.add(register)
        session.commit()
        session.refresh(register)

        print("Update: ", register)

def delete_register(id:int):
    with Session(engine) as session:
        register = session.get(User, id)

        if register is None:
            print(f"Not found id delete {id}")
            return
        
        session.delete(register)
        session.commit()
        print(f"Registro eliminado con id={id}")



def reade_register() -> Sequence[User]:
    with Session(engine) as session:
        registers = session.exec(select(User)).all()
        return registers
    
