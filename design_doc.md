# SkillBridge — Design Document

## Problem Statement
Students and early-career professionals struggle to identify the gap between their current skills and job requirements. Existing tools are either too generic or require navigating multiple platforms.

## Solution
SkillBridge is a web app that takes a user's resume text and a target role, then uses AI to identify matched and missing skills, visualize the gap, and generate a personalized learning roadmap.

## Tech Stack

| Layer | Technology | Reason |
|-------|-----------|--------|
| Backend | FastAPI (Python) | Fast, async, auto-generates API docs |
| Frontend | React + Vite | Fast dev experience, component-based |
| AI | Gemini 1.5 Flash (free tier) | No cost, sufficient for text analysis |
| Fallback | Keyword matching against JSON taxonomy | Transparent, debuggable, always available |
| Testing | Pytest + FastAPI TestClient | Simple, reliable, no extra setup |

## Architecture
```
React Frontend
     ↓ REST API
FastAPI Backend
     ↓ if AI available        ↓ if AI fails
Gemini API              Rule-based fallback
     ↓                        ↓
         JSON response to frontend
```

## AI Integration
The AI feature (Gemini) is used for:
1. **Resume parsing** — extracts skills from unstructured resume text
2. **Gap analysis** — compares extracted skills against role requirements
3. **Roadmap generation** — suggests specific learning resources per missing skill

## Fallback Strategy
If the Gemini API is unavailable or returns malformed JSON, the system falls back to keyword matching — scanning the resume text for skills listed in `skill_taxonomy.json`. This is transparent to the user via a "Powered by: Rule-based fallback" badge.

## Data
All data is synthetic — no real user data or scraped content. Includes:
- `skill_taxonomy.json` — 6 roles with required skills
- `sample_resumes.json` — 3 synthetic candidate profiles

## Future Enhancements
- PDF/image upload with OCR (PyMuPDF + Tesseract)
- PostgreSQL for persistent user sessions
- Real job posting integration
- Mock interview question generator
- Progress tracking dashboard