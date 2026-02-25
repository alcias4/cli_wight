import argparse
from argparse import Namespace

def parser_args() -> Namespace:

    parser = argparse.ArgumentParser(
        prog="app",
        description="CLI to track weight and exercise"
    )

    parser.add_argument(
        "-w", "--weight",
        help="Weight to create/update a record (int or float). Example: 70 or 70.5",
        type=number,
        default=None
    )

    parser.add_argument(
        "-e", "--exercise",
        help='Whether you exercised (true/false). '
            'True: y, yes, si, true, t, 1 | False: n, no, false, f, 0',
        type=strbool,
        default=None
    )

    parser.add_argument(
        "-i", "--id",
        help="Record ID to update or delete. Example: -i 3",
        type=int,
        default=None
    )

    parser.add_argument(
        "--ids",
        help="List of record IDs to delete multiple records. Example: --ids 1 2 3",
        nargs="+",
        default=None
    )

    parser.add_argument(
        "-r", "--reade",
        help="Show records (example: -r y).",
        default=None,
        type=str
    )

    parser.add_argument(
        "-d", "--delete",
        help='Delete record(s) (use with -i or --ids). '
            'Accepts true/false: y, yes, si, true, 1 | n, no, false, 0',
        default=None,
        type=strbool
    )

    parser.add_argument(
        "-g", "--grafic",
        help="Grafic weight vs id or count ex: -g yes or y",
        type=strbool,
        default=None
    )
    

    args = parser.parse_args()
    
    return args

def number(s: str):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            raise argparse.ArgumentTypeError(
                f"{s} not number valido: 3 or 3.14"
            )


def strbool(s: str):
    s = s.lower()

    if s in ["true", "yes", "si", "y", "t", "1"]:
        return True

    if s in ["false", "f", "no", "n", "0"]:
        return False