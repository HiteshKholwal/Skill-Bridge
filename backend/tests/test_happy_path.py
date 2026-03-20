from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app

client = TestClient(app)

mock_ai_response = {
    "matched_skills": ["Python", "SQL"],
    "missing_skills": ["Docker", "AWS"],
    "match_score": 50
}

def test_analyze_happy_path():
    with patch("routers.analyze.analyze_resume", return_value=mock_ai_response):
        response = client.post("/analyze", json={
            "resume_text": "I have experience with Python and SQL. Worked on REST APIs and Git.",
            "target_role": "Backend Engineer"
        })
        assert response.status_code == 200
        data = response.json()
        assert "matched_skills" in data
        assert "missing_skills" in data
        assert "match_score" in data

def test_roadmap_happy_path():
    mock_roadmap = {
        "steps": [
            {"skill": "Docker", "resource": "Docker Docs", "duration": "1 week", "free": True}
        ]
    }
    with patch("routers.roadmap.generate_roadmap", return_value=mock_roadmap):
        response = client.post("/roadmap", json={
            "missing_skills": ["Docker", "AWS"],
            "target_role": "Backend Engineer"
        })
        assert response.status_code == 200
        data = response.json()
        assert "steps" in data