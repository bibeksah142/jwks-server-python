from fastapi import FastAPI, Response
from keys import Key, to_jwk
from jwt_utils import issue_jwt
import time

app = FastAPI()

valid_key = Key("valid-key", ttl_seconds=3600)
expired_key = Key("expired-key", ttl_seconds=-3600)


@app.get("/.well-known/jwks.json")
def jwks():
    keys = []

    if time.time() < valid_key.expiry:
        keys.append(to_jwk(valid_key))

    return {"keys": keys}


@app.post("/auth")
def auth(expired: bool = False):
    key = expired_key if expired else valid_key
    token = issue_jwt(key)
    return {"token": token}
