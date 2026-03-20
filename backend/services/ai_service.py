import os
import json
from dotenv import load_dotenv

load_dotenv()

def get_client():
    from google import genai
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise Exception("No API key provided")
    return genai.Client(api_key=api_key)

async def analyze_resume(resume_text: str, target_role: str) -> dict:
    client = get_client()
    prompt = f"""
You are a career advisor. Analyze this resume and identify skill gaps for the target role.

Resume:
{resume_text}

Target Role: {target_role}

Respond ONLY with a JSON object in this exact format, no extra text:
{{
  "matched_skills": ["skill1", "skill2"],
  "missing_skills": ["skill3", "skill4"],
  "match_score": 72
}}
"""
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )
    text = response.text.strip().replace("```json", "").replace("```", "").strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        raise Exception("AI returned malformed JSON, switching to fallback")

async def generate_roadmap(missing_skills: list, target_role: str) -> dict:
    client = get_client()
    prompt = f"""
You are a career coach. Create a learning roadmap for these missing skills for the role: {target_role}.

Missing skills: {", ".join(missing_skills)}

Respond ONLY with a JSON object in this exact format, no extra text:
{{
  "steps": [
    {{
      "skill": "skill name",
      "resource": "course or resource name",
      "duration": "2 weeks",
      "free": true
    }}
  ]
}}
"""
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )
    text = response.text.strip().replace("```json", "").replace("```", "").strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        raise Exception("AI returned malformed JSON, switching to fallback")