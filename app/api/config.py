import os
from pony.orm import Database
from urllib.parse import urlparse

from .utils.helpers import DatabaseUrl


DATABASE_URI = os.getenv(
    "DATABASE_URL",
    "sqlite://:memory:",
)
PONY_DATABASE_URI = DatabaseUrl(DATABASE_URI).connection_dict()
DEBUG = True
JWT_SECRET = "meia-noite-eu-conto"
