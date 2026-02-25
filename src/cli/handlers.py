from argparse import Namespace
from rich.console import Console
from db.crud import insert_register, update_register,delete_register
from cli.ui import table_info, grafic_ui



console = Console()

def handler_show_data(args:Namespace):
    with console.status("loading", spinner="dots"):
        table_info(args=args) 

        
def handler_insert(args: Namespace):
    with console.status("loading", spinner="dots"):
        if args.id == None and args.weight != None:
            insert_register(weight=args.weight, exercise=args.exercise)

def handler_update(args:Namespace):
    with console.status("loading", spinner="dots"):
        if args.id != None and (args.weight != None or args.exercise != None):
            update_register(id=args.id, weight=args.weight, exercise=args.exercise)

def handler_delete_one(args: Namespace):
    with console.status("loading", spinner="dots"):
        if args.id !=None and args.delete != None: 
            delete_register(id=args.id)

def handler_delete_many(args: Namespace):
    with console.status("loading", spinner="dots"):
        if args.ids !=None and args.delete != None:
            for id in args.ids:
                try: 
                    registers_id = int(id)
                except ValueError:
                    print(f"Not is type int {id}")
                    continue

                delete_register(registers_id)


def handler_show_grafic(args:Namespace):
    with console.status("loading", spinner="dots"):
        if args.grafic is not None:
            grafic_ui()



def process_args(args):
    handler_show_data(args)
    handler_insert(args)
    handler_update(args)
    handler_delete_one(args)
    handler_delete_many(args)
    handler_show_grafic(args)