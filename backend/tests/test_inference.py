from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_weather_inference():
    response = client.post(
        "/inference/",
        json={
            "instruction": "What's the weather in Chennai?"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["tool_call"]["tool_name"] == "get_weather"
    assert data["tool_call"]["arguments"]["location"] == "Chennai"


def test_unknown_instruction():
    response = client.post(
        "/inference/",
        json={
            "instruction": "Tell me a joke"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["tool_call"]["tool_name"] == "unknown"


def test_empty_instruction():
    response = client.post(
        "/inference/",
        json={
            "instruction": ""
        }
    )

    assert response.status_code == 422