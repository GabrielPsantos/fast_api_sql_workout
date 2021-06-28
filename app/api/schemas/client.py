from uuid import UUID
from typing import List, Optional

from pydantic import BaseModel
from .item import Item

class ClientBase(BaseModel):
    client_email: str


class ClientCreate(ClientBase):
    hashed_password: str


class Client(ClientBase):
    client_uuid : str
    is_active: bool
    client_photo_profile: str
    items: List[Item] = []

    class Config:
        orm_mode = True