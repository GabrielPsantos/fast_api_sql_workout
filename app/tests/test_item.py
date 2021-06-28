from pony.orm.core import commit
from starlette.testclient import TestClient
from unittest import TestCase

from pony.orm import db_session

from api.main import app
from api.models.item import Item
from api.models.client import Client
from .test_setup import FastAPIBaseTest


class TestItemRoutes(FastAPIBaseTest):
    client_payload = {
        "client_email": "owner_mail@mail.com",
        "hashed_password": "string",
    }
    item_payload = {
        "title": "fake Title :D",
        "description_body": "blah blah blah blah",
    }

    @db_session
    def test_create_item(self):
        client = Client(**self.client_payload)
        commit()
        params = {"client_uuid": client.client_uuid}

        response = self.app.post(
            "/items/",
            json=self.item_payload,
            params=params
        )
        response_payload = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response_payload.get("description_body"),
            self.item_payload.get("description_body"),
        )

    @db_session
    def test_get_item_list(self):
        client = Client(**self.client_payload)
        commit()
        item1 = Item(**self.item_payload,item_owner=client)
        item2 = Item(**self.item_payload,item_owner=client)
        commit()
        
        response = self.app.get("/items/")
        response_payload = response.json()
        single_item = response_payload[0]
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response_payload), list)
        
        self.assertEqual(len(response_payload), 2)
        self.assertEqual(
            single_item.get("title"),
            item1.title,
        )

