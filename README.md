# SkillBridge — Skill Gap Career Navigator

## Candidate Name: [Hitesh Kholwal]
## Scenario Chosen: Scenario 2 — Skill-Bridge Career Navigator
## Estimated Time Spent: [X] hours

---

## Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- Gemini API key (free at aistudio.google.com)

### Run Commands

**Backend:**
```bash
cd backend
pip install -r requirements.txt
# Add your GEMINI_API_KEY to .env (see .env.example)
python -m uvicorn main:app --reload
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

Visit `http://localhost:5173`

### Test Commands
```bash
cd backend
pytest tests/ -v
```

---

## AI Disclosure
- **Did you use an AI assistant?** Yes — Claude (Anthropic)
- **How did you verify suggestions?** Ran all code manually, tested each endpoint via Swagger UI at `/docs`, verified edge cases through pytest, and checked fallback behavior by simulating API failures.
- **One example of a suggestion I rejected or changed:** Claude initially suggested using `google.generativeai` package — I switched to the newer `google.genai` package after identifying it was deprecated.

---

## Tradeoffs & Prioritization

### What I cut to stay within the timebox:
- **Resume file upload (PDF/image):** Would use PyMuPDF for PDF parsing and Tesseract OCR for images. Cut in favor of text input to focus on the core AI pipeline.
- **User authentication:** No login system. In production, would add JWT-based auth.
- **Persistent database:** Used JSON files instead of PostgreSQL to avoid setup overhead.
- **Streaming AI responses:** Responses load all at once. Would use server-sent events for better UX.

### What I would build next:
- PDF/image resume upload with OCR
- User accounts to save and track progress over time
- Integration with real job posting APIs (LinkedIn, Indeed)
- Mock interview question generator based on skill gaps
- Email notifications for roadmap reminders

### Known Limitations:
- Gemini free tier has rate limits — may occasionally fall back to rule-based analysis
- Skill matching is case-sensitive in fallback mode
- Target roles limited to 6 predefined options
- No persistent storage between sessions

---

## Video
[https://youtu.be/9dUBvcDcoFo]
