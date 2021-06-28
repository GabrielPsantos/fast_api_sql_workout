from uuid import UUID
from passlib.hash import bcrypt
from pony.orm import db_session, select, commit
from pony.orm.serialization import to_dict
from ..models.client import Client
from ..models.item import Item
from ..schemas.item import ItemCreate
from ..schemas.client import ClientCreate


@db_session
def get_client(client_uuid: UUID):
    client = Client.get(client_uuid=client_uuid)
    if client:
        return client.to_dict(exclude=["hashed_password", "items"])
    return None


@db_session
def get_client_by_email(client_email: str):
    client = Client.get(client_email=client_email)
    if client:
        return client.to_dict(exclude=["hashed_password", "items"])
    return None


@db_session
def get_clients(skip: int = 0, limit: int = 100):
    clients = Client.select().order_by(Client.client_uuid)[skip:limit]
    return Client.list_to_dict(clients)


@db_session
def create_client(client: ClientCreate):
    exclude = ["hashed_password", "items"]
    hashed_password = client.hashed_password
    cli = Client(
        client_email=client.client_email,
        hashed_password=bcrypt.hash(hashed_password),
    )
    commit()
    return cli.to_dict(exclude=exclude)
