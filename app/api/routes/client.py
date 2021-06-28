import uuid
from fastapi import APIRouter, Depends, HTTPException
from pony.orm.serialization import to_dict
from ..schemas.client import ClientCreate, Client as ClientSchema
from ..actions import client as actions
from ..actions import auth as authentication

router = APIRouter(
    prefix="/clients",
    tags=["clients"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
def create_client(client: ClientCreate):
    db_client = actions.get_client_by_email(client_email=client.client_email)
    if db_client:
        raise HTTPException(status_code=400, detail="Email already registered")
    return actions.create_client(client=client)


@router.get("/")
def read_clients(skip: int = 0, limit: int = 100):
    clients = actions.get_clients(skip=skip, limit=limit)
    return clients

@router.get("/me")
def get_my_user(client: ClientSchema = Depends(authentication.get_current_client)):
    return client.to_dict(exclude=["hashed_password"])

@router.get("/{client_uuid}")
def read_client(client_uuid: str):
    client_uuid = uuid.UUID(client_uuid).hex
    db_client = actions.get_client(client_uuid=client_uuid)
    if db_client is None:
        raise HTTPException(status_code=404, detail="client not found")
    return db_client

