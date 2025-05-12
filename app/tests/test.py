from fastapi.testclient import TestClient
from app.main import app
import time

client = TestClient(app)


def test_token_generation():
    username = "testuser"
    response = client.post(f"/token/{username}")
    assert response.status_code == 200
    assert "token" in response.json()


def test_validation():
    username = "testuser"
    response = client.post(f"/token/{username}")
    token = response.json()["token"]

    get_response = client.get("/check/", headers={"Token": token})
    assert get_response.status_code == 200
    assert get_response.json()["message"] == "authorized content"


def test_token_expiry():
    username = "testuser"
    response = client.post(f"/token/{username}")
    token = response.json()["token"]
    print("\nSleep for 60 seconds")
    time.sleep(61)  # tested with expiry time = 1 minute
    get_response = client.get("/check/", headers={"Token": token})
    assert get_response.status_code == 401
    assert get_response.json()["message"] == "invalid token"
