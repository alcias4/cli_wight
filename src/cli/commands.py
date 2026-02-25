import argparse
from argparse import Namespace

def parser_args() -> Namespace:
    parser = argparse.ArgumentParser(prog="app", description="Mi cli")
    parser.add_argument("-w", "--weight", help="your weight and enter a number type int(3) o float(3.14)", type=number, default=None)
    parser.add_argument("-e", 
                        "--exercise", 
                        help='Enter if did ejercise: False: ["false", "f", "no", "n", "0"]  o True:["true", "yes", "si", "y", "t", "1"] ', 
                        type=strbool, 
                        default=None)
    parser.add_argument("-i", "--id", help="for update a register with the id", type=int, default=None)
    parser.add_argument("--ids", help="list of ids for remove multiple register ", nargs="+", default=None)

    parser.add_argument("-r", "--reade", help="reade register all", default=None, type=str)
    parser.add_argument("-d", "--delete", help='Delete bool + id = remove register in position : False: ["false", "f", "no", "n", "0"]  o True:["true", "yes", "si", "y", "t", "1"] ', default=None, type=strbool)

    

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