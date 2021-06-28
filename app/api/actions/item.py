from uuid import UUID
from pony.orm import db_session, select
from pony.orm.serialization import to_dict
from ..models.item import Item
from ..models.client import Client
from ..schemas.item import ItemCreate


@db_session
def get_items(skip: int = 0, limit: int = 100):
    items = Item.select().order_by(Item.item_uuid)[skip:limit]
    return Item.list_to_dict(items)


@db_session
def create_client_item(item: ItemCreate, client_uuid: UUID):
    client = Client.get(client_uuid=client_uuid)
    if not client:
        return None
    else:
        item = Item(
            title=item.title,
            description_body=item.description_body,
            item_owner=client,
        )
    return item.to_dict()
