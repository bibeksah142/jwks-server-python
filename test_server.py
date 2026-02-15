from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_jwks_returns_key():
    r = client.get("/.well-known/jwks.json")
    assert r.status_code == 200
    assert "keys" in r.json()


def test_auth_returns_token():
    r = client.post("/auth")
    assert r.status_code == 200
    assert "token" in r.json()


def test_auth_expired():
    r = client.post("/auth?expired=true")
    assert r.status_code == 200
    assert "token" in r.json()
