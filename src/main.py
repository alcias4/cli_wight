import argparse
from db.db import create_db

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



def main():
    create_db()
    parser = argparse.ArgumentParser(prog="app", description="Mi cli")
    parser.add_argument("-w", "--weight", help="your weight and enter a number type int(3) o float(3.14)", type=number)
    parser.add_argument("-e", "--exercise", help="Enter if did ejercise: yes or not", default=False)


    args = parser.parse_args()
    
    
    print(f"{args}")

if __name__ == "__main__":
    main()
