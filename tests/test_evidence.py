from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_and_get_evidence():
    payload = {"msg": "test"}

    response = client.post("/api/evidence", json=payload)

    print(response.json())
    print(response.status_code)

    assert response.status_code == 200
    evidence_id = response.json()["id"]

    response = client.get(f"/api/evidence/{evidence_id}")
    assert response.status_code == 200
    assert response.json()["data"] == payload


