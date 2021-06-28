from pony.orm.core import commit
from starlette.testclient import TestClient
from unittest import TestCase

from pony.orm import db_session

from api.main import app
from api.models.client import Client
from .test_setup import FastAPIBaseTest


class TestClientRoutes(FastAPIBaseTest):
    client_payload = {
        "client_email": "mail_test@mail.com",
        "hashed_password": "string",
    }

    def test_create_client(self):
        response = self.app.post("/clients/", json=self.client_payload)
        response_payload = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response_payload.get("client_email"),
            self.client_payload.get("client_email"),
        )

    @db_session
    def test_get_client_list(self):
        Client(**self.client_payload)
        commit()

        response = self.app.get("/clients/")
        response_payload = response.json()
        single_user = response_payload[0]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response_payload), list)
        self.assertEqual(len(response_payload), 1)
        self.assertEqual(
            single_user.get("client_email"),
            self.client_payload.get("client_email"),
        )

    @db_session
    def test_get_client_by_uuid(self):
        client = Client(**self.client_payload)
        commit()

        uuid = client.client_uuid
        response = self.app.get(f"/clients/{uuid}")
        response_payload = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response_payload.get("client_email"),
            client.client_email,
        )
