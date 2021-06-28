import os
from typing import Dict
from urllib.parse import urlparse


class DatabaseUrl:
    def __init__(self, url: str = None, url_env_name: str = None) -> None:
        self.host = None
        url = url or os.environ.get(url_env_name)
        if "sqlite" in url:
            self.provider = "sqlite"
            self.filename = "testdb"
            self.create_db = True
        else:
            parsed_url = urlparse(url)
            auth, host = parsed_url.netloc.split("@")
            if len(auth.split(":")) == 1:
                user = auth
                password = None
            else:
                user, password = auth.split(":")
            self.provider = parsed_url.scheme
            self.user = user
            self.password = password
            self.host = host
            self.database = parsed_url.path.lstrip("/")


    def connection_dict(self) -> Dict:
        if "sqlite" not in self.provider:
            conn_dict = {
                "provider": self.provider,
                "user": self.user,
                "password": self.password,
                "host": self.host,
                "database": self.database,
            }
        else:
            conn_dict = {
                "provider": self.provider,
                "filename": self.filename,
                "create_db": self.create_db,
            }
        if self.host and len(self.host.split(":")) > 1:
            conn_dict.update(
                {
                    "host": self.host.split(":")[0],
                    "port": self.host.split(":")[1],
                }
            )
        return conn_dict
