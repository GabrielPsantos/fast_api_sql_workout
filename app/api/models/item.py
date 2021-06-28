import uuid
from pony.orm.core import Required, PrimaryKey, Set, Optional
from typing import Dict, List
from ..utils.database import db

from .client import Client


class Item(db.Entity):
    item_uuid = PrimaryKey(uuid.UUID, default=uuid.uuid4)
    title = Required(str)
    description_body = Required(str)
    item_owner = Required(Client)
    _table_ = "item"
    
    def to_dict(self, *argv) -> Dict:
        obj = super(Item, self).to_dict(*argv)
        id = obj.get("item_uuid", None)
        if type(id) == uuid.UUID:
            obj.update({
                "item_uuid": str(id)
            })
        return obj

    @staticmethod
    def list_to_dict(item_list) -> List:
        return [x.to_dict() for x in item_list]