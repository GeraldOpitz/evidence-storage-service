"""Integration tests for evidence endpoints."""

import os

import httpx

BASE_URL = os.getenv("TEST_BASE_URL", "http://localhost:8000")


def test_create_and_get_evidence():
    payload = {"msg": "test"}

    create_response = httpx.post(
        f"{BASE_URL}/api/evidence",
        json=payload,
        timeout=10.0,
    )

    assert create_response.status_code == 200
    body = create_response.json()
    assert "id" in body

    evidence_id = body["id"]

    get_response = httpx.get(
        f"{BASE_URL}/api/evidence/{evidence_id}",
        timeout=10.0,
    )

    assert get_response.status_code == 200
    assert get_response.json()["data"] == payload
