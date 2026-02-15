import jwt
import time
from cryptography.hazmat.primitives import serialization


def issue_jwt(key):
    payload = {
        "sub": "fake-user",
        "iss": "jwks-server",
        "iat": int(time.time()),
        "exp": key.expiry,
    }

    private_pem = key.private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )

    token = jwt.encode(
        payload,
        private_pem,
        algorithm="RS256",
        headers={"kid": key.kid},
    )
    return token
