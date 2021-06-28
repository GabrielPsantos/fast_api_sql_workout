from pony.orm.core import commit
from starlette.testclient import TestClient
from unittest import TestCase

from pony.orm import db_session

from api.main import app
from api.models.item import Item
from api.models.client import Client

client = TestClient(app)


class FastAPIBaseTest(TestCase):
    default_client = {
        "client_email": "mail@mail.com",
        "hashed_password": "senha@123",
    }

    def setUp(self) -> None:
        self.app = client

    @db_session
    def tearDown(self) -> None:
        Client.select().delete(bulk=True)
        Item.select().delete(bulk=True)
