from fastapi import APIRouter
from pydantic import BaseModel
from services.ai_service import analyze_resume
from services.fallback_service import fallback_analyze

router = APIRouter()

class ResumeInput(BaseModel):
    resume_text: str
    target_role: str

@router.post("/analyze")
async def analyze(input: ResumeInput):
    if not input.resume_text.strip():
        return {"error": "Resume text cannot be empty"}
    if not input.target_role.strip():
        return {"error": "Target role cannot be empty"}
    if len(input.resume_text) < 20:
        return {"error": "Resume text too short to analyze"}

    try:
        result = await analyze_resume(input.resume_text, input.target_role)
        return {"source": "ai", **result}
    except Exception as e:
        print(f"AI failed, using fallback: {e}")
        result = fallback_analyze(input.resume_text, input.target_role)
        return {"source": "fallback", **result}