"""Integration test for health endpoint."""

import os

import httpx

BASE_URL = os.getenv("TEST_BASE_URL", "http://localhost:8000")


def test_health():
    response = httpx.get(f"{BASE_URL}/health", timeout=10.0)

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
