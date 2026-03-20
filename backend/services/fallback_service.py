import json
import os

def load_taxonomy():
    path = os.path.join(os.path.dirname(__file__), "..", "data", "skill_taxonomy.json")
    with open(path) as f:
        return json.load(f)

def fallback_analyze(resume_text: str, target_role: str) -> dict:
    taxonomy = load_taxonomy()
    resume_lower = resume_text.lower()

    role_data = None
    for role in taxonomy["roles"]:
        if target_role.lower() in role["title"].lower():
            role_data = role
            break

    if not role_data:
        role_data = taxonomy["roles"][0]

    required_skills = role_data["required_skills"]
    matched = [s for s in required_skills if s.lower() in resume_lower]
    missing = [s for s in required_skills if s.lower() not in resume_lower]
    score = int((len(matched) / len(required_skills)) * 100) if required_skills else 0

    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "match_score": score
    }

def fallback_roadmap(missing_skills: list, target_role: str) -> dict:
    resources = {
        "python": {"resource": "Python for Everybody - Coursera", "duration": "4 weeks", "free": True},
        "sql": {"resource": "SQLZoo", "duration": "1 week", "free": True},
        "machine learning": {"resource": "Andrew Ng ML Course - Coursera", "duration": "8 weeks", "free": True},
        "docker": {"resource": "Docker Getting Started Docs", "duration": "1 week", "free": True},
        "aws": {"resource": "AWS Cloud Practitioner Essentials", "duration": "3 weeks", "free": True},
        "react": {"resource": "React Official Docs Tutorial", "duration": "2 weeks", "free": True},
        "git": {"resource": "Pro Git Book", "duration": "3 days", "free": True},
    }

    steps = []
    for skill in missing_skills:
        match = resources.get(skill.lower(), {
            "resource": f"Search '{skill}' on freeCodeCamp or YouTube",
            "duration": "2 weeks",
            "free": True
        })
        steps.append({"skill": skill, **match})

    return {"steps": steps}