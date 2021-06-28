import jwt
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pony.orm.serialization import to_dict
from ..actions import auth as actions
from ..config import JWT_SECRET

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


@router.post("/token")
def generate_token(form_data: OAuth2PasswordRequestForm = Depends()):

    client = actions.authenticate_client(form_data.username, form_data.password)
    if not client:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )
    token = jwt.encode(client.to_dict(), JWT_SECRET)
    return {"access_token": token, "token_type": "bearer"}
