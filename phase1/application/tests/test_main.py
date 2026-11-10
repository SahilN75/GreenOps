
import pytest
from fastapi.testclient import TestClient
from app.main import app, deployments

client = TestClient(app)

@pytest.fixture(autouse=True)
def reset_deployments():
    deployments.clear()
    yield
    deployments.clear()

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["project"] == "GreenOps"

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_create_deployment():
    response = client.post("/api/v1/deployments", json={
        "application_name": "test-app",
        "image": "nginx:latest",
        "cpu_cores": 0.5,
        "memory_mb": 512
    })
    assert response.status_code == 201
    assert response.json()["status"] == "PENDING"

def test_list_deployments():
    client.post("/api/v1/deployments", json={
        "application_name": "test-app",
        "image": "nginx:latest",
        "cpu_cores": 0.5,
        "memory_mb": 512
    })
    response = client.get("/api/v1/deployments")
    assert response.status_code == 200
    assert response.json()["total"] == 1

def test_invalid_cpu():
    response = client.post("/api/v1/deployments", json={
        "application_name": "test-app",
        "image": "nginx:latest",
        "cpu_cores": 5,
        "memory_mb": 512
    })
    assert response.status_code == 422

def test_missing_deployment():
    response = client.get("/api/v1/deployments/nonexistent")
    assert response.status_code == 404
