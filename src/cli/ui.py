from argparse import Namespace
from db.crud import reade_register
from rich.console import Console
from rich.table import  Table
import plotext as plt

def table_info(args: Namespace ):
    if args.reade == "yes":
        console = Console()
        table = Table(title="Infomation progress")
        table.add_column("ID", style="cyan", no_wrap=True, justify="center")
        table.add_column("Weight", style="cyan", justify="center")
        table.add_column("Exercise", style="cyan", no_wrap=True, justify="center")
        table.add_column("Difference", style="cyan", no_wrap=True, justify="center")



        registers = reade_register()
        for re in registers:
            exercise: str
            difference: str
            if re["exercise"] == True:
                exercise = f"[green]{re["exercise"]}[/green]"
            else:
                exercise = f"[red]{re["exercise"]}[/red]"
            
            if re["difference"] > 0.0:
                difference = f"[green]{re["difference"]}[/green]"
            elif re["difference"] < 0.0:
                difference = f"[red]{re["difference"]}[/red]"
            else:
                difference = f"[white]{re["difference"]}[/white]"

            table.add_row(str(re["id"]), str(re["weight"]), exercise,  difference)


        console.print(table)


def grafic_ui():
    registers = reade_register()

    weight = []
    id =  []
    for row in registers:
        weight.append(float(row["weight"]))
        id.append(int(row["id"]))

    if len(weight) > 0:
        plt.clear_figure()  
        plt.plot(id, weight)

        if len(weight) < 5:
            plt.plotsize(30, 10)
        elif len(weight) < 10:
            plt.plotsize(50, 20)

        plt.title("weight trend")
        plt.xlabel("Day")
        plt.ylabel("Weight (kg)")
        plt.show()
    else:
        print("No hay datos para graficar")