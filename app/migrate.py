import os
import typer
import logging
from yoyo import read_migrations, get_backend

from api.config import DATABASE_URI

def main():
    try:
        backend = get_backend(DATABASE_URI)
        print(DATABASE_URI)
        migrations = read_migrations("./migrations")
        backend.apply_migrations(backend.to_apply(migrations))
    except Exception as e:
        logging.error(f"Error on execute migrations {e}")
        print("Error on execute migrations D:")
    
if __name__ == "__main__":
    typer.run(main)