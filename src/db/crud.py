from sqlmodel import create_engine, Session, select
from db.db import engine
from models.models import User
from rich.console import Console

console = Console()


def insert_register(weight: float, exercise: bool):
    with Session(engine) as session:
        register = User(exercise=exercise, weight=weight)
        session.add(register)
        session.commit()
        session.refresh(register)

        print("insert: ", register)
    cal_defference_colum()

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
    cal_defference_colum()

def delete_register(id:int):
    with Session(engine) as session:
        register = session.get(User, id)

        if register is None:
            print(f"Not found id delete {id}")
            return
        
        session.delete(register)
        session.commit()
        print(f"Registro eliminado con id={id}")

    cal_defference_colum()

def reade_register() -> list[dict]:
    with Session(engine) as session:
        registers = session.exec(select(User).order_by(User.id)).all() # type: ignore

        rows = []
        for r in registers:
            rows.append({
                "id": r.id,
                "weight": r.weight,
                "exercise": r.exercise,
                "difference": r.difference,
            })
        return rows

        

def cal_defference_colum():
    with Session(engine) as session:
        registers = session.exec(
            select(User).order_by(User.id) # type: ignore
        ).all()

        previous_weight = None
        for row in registers:
            if row.weight is None:
                row.difference = None
            elif previous_weight is  None:
                row.difference = 0.0
                previous_weight = row.weight
            else:
                row.difference =   round(previous_weight - row.weight, 2)
                previous_weight = row.weight

            session.add(row)
        session.commit()