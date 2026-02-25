
from db.db import create_db
from cli.commands import parser_args
from cli.handlers import process_args

def main():
    create_db()
    args = parser_args()
    process_args(args=args)

if __name__ == "__main__":
    main()
