# JWKS Server (Python Implementation)

## Overview
This project implements a simple RESTful JSON Web Key Set (JWKS) server.  
The server generates RSA key pairs, assigns each key a unique Key ID (`kid`) and expiration time, and exposes endpoints to retrieve public keys and issue JSON Web Tokens (JWTs).

This project is for educational purposes and demonstrates how authentication systems use JWKS to validate JWT signatures.

---
## Project Structure 

jwks-server-python/
│
├── app.py            # FastAPI server and routes
├── keys.py           # RSA key generation and JWKS formatting
├── jwt_utils.py      # JWT signing logic
├── test_server.py    # Automated tests
├── requirements.txt  # Dependencies
└── README.md

## Features

- RSA key pair generation (2048-bit)
- Unique `kid` assigned to each key
- Key expiration handling
- JWKS endpoint serving only **non-expired** public keys
- `/auth` endpoint issuing signed JWTs
- Support for issuing tokens signed with **expired keys** via query parameter
- RESTful API using FastAPI
- Automated test suite with >80% coverage

---

## Technologies Used

- Python 3
- FastAPI (REST API framework)
- Uvicorn (ASGI server)
- cryptography (RSA key generation)
- PyJWT (JWT creation)
- pytest (testing framework)

---
## Screenshot
file path : `/screenshot`
## How It Works

1. The server generates two RSA key pairs at startup:
   - A **valid key** (used normally)
   - An **expired key** (used only when requested)

2. Each key includes:
   - `kid` (Key ID)
   - Expiration timestamp

3. The JWKS endpoint publishes only currently valid public keys.

4. The `/auth` endpoint issues JWTs signed with:
   - The valid key (default)
   - The expired key (when `?expired=true` is provided)

---

## Running the Server

### Install Dependencies

```bash
python3 -m pip install -r requirements.txt
