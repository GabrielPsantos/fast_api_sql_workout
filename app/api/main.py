import uuid
from typing import List
from pony.orm import Database
from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse

from .routes import item, client, auth
from .utils.database import db

app = FastAPI()

app.include_router(item.router)
app.include_router(client.router)
app.include_router(auth.router)

db.generate_mapping(check_tables=False)
