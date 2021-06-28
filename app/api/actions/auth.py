import jwt
from pony.orm import db_session
from pony.orm.serialization import to_dict
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from ..models.client import Client
from ..config import JWT_SECRET

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token", auto_error=False)


@db_session
def authenticate_client(client_email: str, password: str):
    client = Client.get(client_email=client_email)
    if not client:
        return False
    if not client.verify_password(password):
        return False
    return client


@db_session
def get_current_client(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        client = Client.get(client_uuid=payload.get("client_uuid"))
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )
    return client
