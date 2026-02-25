from argparse import Namespace
from db.crud import reade_register
from rich.console import Console
from rich.table import  Table

def table_info(args: Namespace ):
    if args.reade == "yes":
        console = Console()
        table = Table(title="Infomation progress")
        table.add_column("ID", style="cyan", no_wrap=True)
        table.add_column("Weight", style="cyan")
        table.add_column("Exercise", style="cyan", no_wrap=True)


        registers = reade_register()
        for re in registers:
            exercise: str = ""
            if re.exercise == True:
                exercise = f"[green]{re.exercise}[/green]"
            else:
                exercise = f"[red]{re.exercise}[/red]"
            table.add_row(str(re.id), str(re.weight), exercise)


        console.print(table)