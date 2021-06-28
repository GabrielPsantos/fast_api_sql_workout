from pony.orm import Database, db_session
from ..config import PONY_DATABASE_URI

base_args = PONY_DATABASE_URI

db = Database(base_args)
