from fastapi import APIRouter
from pydantic import BaseModel
from services.ai_service import generate_roadmap
from services.fallback_service import fallback_roadmap

router = APIRouter()

class RoadmapInput(BaseModel):
    missing_skills: list[str]
    target_role: str

@router.post("/roadmap")
async def roadmap(input: RoadmapInput):
    if not input.missing_skills:
        return {"error": "No missing skills provided"}
    try:
        result = await generate_roadmap(input.missing_skills, input.target_role)
        return {"source": "ai", **result}
    except Exception as e:
        print(f"AI failed, using fallback: {e}")
        result = fallback_roadmap(input.missing_skills, input.target_role)
        return {"source": "fallback", **result}