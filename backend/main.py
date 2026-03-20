from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import analyze, roadmap

app = FastAPI(title="SkillBridge API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analyze.router)
app.include_router(roadmap.router)

@app.get("/")
def root():
    return {"status": "SkillBridge API is running"}