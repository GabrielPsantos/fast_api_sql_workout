from pony.orm.core import commit
from starlette.testclient import TestClient
from unittest import TestCase

from pony.orm import db_session
from fastapi import FastAPI, Depends, HTTPException, status

from api.main import app
from api.models.client import Client
from .test_setup import FastAPIBaseTest


class TestBasicAuth(FastAPIBaseTest):
    def test_basic_auth(self):
        client = self.app.post("/clients/", json=self.default_client).json()

        auth_payload = {
            "username": self.default_client["client_email"],
            "password": self.default_client["hashed_password"],
        }
        login = self.app.post("/auth/token", data=auth_payload).json()

        self.assertIn("access_token", login)
        self.assertIn("token_type", login)

        auth = {"Authorization": f'Bearer {login["access_token"]}'}

        me = self.app.get("/clients/me", headers=auth).json()
        self.assertDictEqual(me, client)

    def test_basic_auth_wrong_pass(self):
        client = self.app.post("/clients/", json=self.default_client).json()

        auth_payload = {
            "username": self.default_client["client_email"],
            "password": "eita nenem, esquecia a senha rs",
        }
        login = self.app.post("/auth/token", data=auth_payload)

        self.assertEqual(login.status_code, status.HTTP_401_UNAUTHORIZED)
