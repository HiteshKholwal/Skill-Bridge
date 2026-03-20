from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app

client = TestClient(app)

def test_empty_resume():
    response = client.post("/analyze", json={
        "resume_text": "",
        "target_role": "Backend Engineer"
    })
    assert response.status_code == 200
    assert response.json()["error"] == "Resume text cannot be empty"

def test_short_resume():
    response = client.post("/analyze", json={
        "resume_text": "Hi",
        "target_role": "Backend Engineer"
    })
    assert response.status_code == 200
    assert response.json()["error"] == "Resume text too short to analyze"

def test_empty_target_role():
    response = client.post("/analyze", json={
        "resume_text": "I have experience with Python and SQL.",
        "target_role": ""
    })
    assert response.status_code == 200
    assert response.json()["error"] == "Target role cannot be empty"

def test_ai_failure_fallback():
    with patch("routers.analyze.analyze_resume", side_effect=Exception("API unavailable")):
        response = client.post("/analyze", json={
            "resume_text": "I have experience with Python, SQL, REST APIs, Git and PostgreSQL.",
            "target_role": "Backend Engineer"
        })
        assert response.status_code == 200
        data = response.json()
        assert data["source"] == "fallback"
        assert "matched_skills" in data

def test_empty_missing_skills():
    response = client.post("/roadmap", json={
        "missing_skills": [],
        "target_role": "Backend Engineer"
    })
    assert response.status_code == 200
    assert response.json()["error"] == "No missing skills provided"

def test_malformed_ai_response_fallback():
    with patch("routers.analyze.analyze_resume", side_effect=Exception("AI returned malformed JSON, switching to fallback")):
        response = client.post("/analyze", json={
            "resume_text": "I have experience with Python, SQL, REST APIs, Git and PostgreSQL.",
            "target_role": "Backend Engineer"
        })
        assert response.status_code == 200
        data = response.json()
        assert data["source"] == "fallback"
        assert "matched_skills" in data