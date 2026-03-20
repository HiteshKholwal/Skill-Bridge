import { useState } from "react"
import axios from "axios"

const SAMPLE_RESUME = `Software engineer with 2 years of experience. 
Proficient in Python, REST APIs, and Git. 
Built and deployed web applications using Flask and PostgreSQL.
Familiar with agile development and code reviews.`

export default function Upload({ setAnalysisResult, setRoadmapResult, setPage }) {
  const [resumeText, setResumeText] = useState("")
  const [targetRole, setTargetRole] = useState("")
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState("")

  const handleAnalyze = async () => {
    setError("")
    setLoading(true)
    try {
      const analysisRes = await axios.post("http://127.0.0.1:8000/analyze", {
        resume_text: resumeText,
        target_role: targetRole
      })

      if (analysisRes.data.error) {
        setError(analysisRes.data.error)
        setLoading(false)
        return
      }

      setAnalysisResult({ ...analysisRes.data, targetRole })

      const roadmapRes = await axios.post("http://127.0.0.1:8000/roadmap", {
        missing_skills: analysisRes.data.missing_skills,
        target_role: targetRole
      })

      setRoadmapResult(roadmapRes.data)
      setPage("dashboard")
    } catch (err) {
      setError("Could not connect to server. Make sure the backend is running.")
    }
    setLoading(false)
  }

  return (
    <div className="card">
      <h2>Analyze Your Resume</h2>
      <p style={{ color: "#555", marginBottom: "1rem" }}>
        Paste your resume below and select a target role to see your skill gaps.
      </p>
      <button className="btn" style={{ marginTop: 0, marginBottom: "1rem", background: "#1a1a2e" }}
        onClick={() => setResumeText(SAMPLE_RESUME)}>
        Load Sample Resume
      </button>
      <textarea
        placeholder="Paste your resume text here..."
        value={resumeText}
        onChange={e => setResumeText(e.target.value)}
      />
     <select
  value={targetRole}
  onChange={e => setTargetRole(e.target.value)}
  style={{
    width: "100%", padding: "0.8rem", border: "1px solid #ddd",
    borderRadius: "8px", fontSize: "0.95rem", marginTop: "1rem",
    background: "#f9f9f9", color: "#222", cursor: "pointer",
    appearance: "auto"
  }}
>
  <option value="" disabled>Select a target role...</option>
  <option value="Backend Engineer">Backend Engineer</option>
  <option value="Frontend Engineer">Frontend Engineer</option>
  <option value="Data Engineer">Data Engineer</option>
  <option value="ML Engineer">ML Engineer</option>
  <option value="DevOps Engineer">DevOps Engineer</option>
  <option value="Full Stack Engineer">Full Stack Engineer</option>
</select>
      {error && <p className="error">{error}</p>}
      <button className="btn" onClick={handleAnalyze} disabled={loading}>
        {loading ? "Analyzing..." : "Analyze Skills"}
      </button>
    </div>
  )
}