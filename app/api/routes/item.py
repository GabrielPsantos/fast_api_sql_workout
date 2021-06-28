import uuid
from fastapi import APIRouter, Depends, HTTPException
from ..schemas.item import ItemCreate
from ..actions import item as actions

router = APIRouter(
    prefix="/items",
    tags=["clients"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
def create_item_for_client(client_uuid: str, item: ItemCreate):
    client_uuid = uuid.UUID(client_uuid).hex
    return actions.create_client_item(item=item, client_uuid=client_uuid)

@router.get("/")
def read_items(skip: int = 0, limit: int = 100):
    items = actions.get_items(skip=skip, limit=limit)
    return items
