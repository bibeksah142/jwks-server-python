from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import base64
import time


class Key:
    def __init__(self, kid: str, ttl_seconds: int):
        self.kid = kid
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        self.public_key = self.private_key.public_key()
        self.expiry = int(time.time()) + ttl_seconds


def base64url_uint(val: int) -> str:
    return base64.urlsafe_b64encode(
        val.to_bytes((val.bit_length() + 7) // 8, "big")
    ).rstrip(b"=").decode()


def to_jwk(key: Key) -> dict:
    pub = key.public_key.public_numbers()
    return {
        "kty": "RSA",
        "use": "sig",
        "alg": "RS256",
        "kid": key.kid,
        "n": base64url_uint(pub.n),
        "e": base64url_uint(pub.e),
    }
