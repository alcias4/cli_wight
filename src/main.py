
from db.db import create_db
from crud import insert_register, update_register, reade_register,delete_register
from parser_args import parser_args

def main():
    create_db()
    

    args = parser_args()
    
    if args.reade == "yes":
        print("------ Registers ------")
        registers = reade_register()
        for re in registers:
            print(re)
        print("------------------------")


    # insertar registros
    if args.id == None and (args.weight != None or args.exercise != None ):
        insert_register(weight=args.weight, exercise=args.exercise)
    
    if args.id != None and (args.weight != None or args.exercise != None):
        update_register(id=args.id, weight=args.weight, exercise=args.exercise)

    if args.id !=None and args.delete != None: 
        delete_register(id=args.id)

    
    if args.ids !=None and args.delete != None:
        for id in args.ids:
            try: 
                registers_id = int(id)
            except ValueError:
                print(f"Not is type int {id}")
                continue

            delete_register(registers_id)

if __name__ == "__main__":
    main()
