import uuid
from pony.orm.core import Required, PrimaryKey, Set, Optional
from typing import Dict, List
from ..utils.database import db
from passlib.hash import bcrypt

class Client(db.Entity):
    client_uuid = PrimaryKey(uuid.UUID, default=uuid.uuid4)
    client_email = Required(str, unique=True)
    hashed_password = Required(str)
    client_photo_profile = Optional(str)
    is_active = Optional(bool, default=True)
    items = Set("Item", reverse="item_owner")
    _table_ = "client"
    
    def to_dict(self, *args,**kwargs) -> Dict:
        obj = super(Client, self).to_dict(*args,**kwargs)
        id = obj.get("client_uuid", None)
        if type(id) == uuid.UUID:
            obj.update({
                "client_uuid": str(id)
            })
        return obj
    
    def verify_password(self, password):
        return bcrypt.verify(password, self.hashed_password)

    @staticmethod
    def list_to_dict(client_list, to_exclude=["hashed_password", "items"]) -> List:
        return [x.to_dict(exclude=to_exclude) for x in client_list]

