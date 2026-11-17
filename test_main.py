import hashlib

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_generate_returns_md5_checksum_for_text():
    response = client.post("/generate/", json={"text": "hello"})

    assert response.status_code == 200
    assert response.json() == {"checksum": hashlib.md5(b"hello").hexdigest()}


def test_generate_returns_md5_checksum_for_empty_text():
    response = client.post("/generate/", json={"text": ""})

    assert response.status_code == 200
    assert response.json() == {"checksum": hashlib.md5(b"").hexdigest()}


def test_generate_rejects_missing_text_field():
    response = client.post("/generate/", json={})

    assert response.status_code == 422
