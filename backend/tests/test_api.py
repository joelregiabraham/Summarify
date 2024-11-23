import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_summarize_endpoint():
    response = client.post(
        "/api/summarize",
        json={
            "content": "This is a test content that needs to be summarized.",
            "summary_length": "short",
            "complexity_level": "simple"
        }
    )
    assert response.status_code == 200
    assert "summary" in response.json()