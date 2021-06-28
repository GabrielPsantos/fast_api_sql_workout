from uuid import UUID
from typing import List, Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description_body: str = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    item_uuid: str
    owner_uuid: str

    class Config:
        orm_mode = True

