import { useState } from "react"
import Upload from "./pages/Upload"
import Dashboard from "./pages/Dashboard"
import Roadmap from "./pages/Roadmap"
import "./App.css"

function App() {
  const [page, setPage] = useState("upload")
  const [analysisResult, setAnalysisResult] = useState(null)
  const [roadmapResult, setRoadmapResult] = useState(null)

  return (
    <div className="app">
      <nav className="navbar">
        <h1>SkillBridge</h1>
        <div className="nav-links">
          <button onClick={() => setPage("upload")} className={page === "upload" ? "active" : ""}>Resume</button>
          <button onClick={() => setPage("dashboard")} className={page === "dashboard" ? "active" : ""} disabled={!analysisResult}>Gap Analysis</button>
          <button onClick={() => setPage("roadmap")} className={page === "roadmap" ? "active" : ""} disabled={!roadmapResult}>Roadmap</button>
        </div>
      </nav>

      <main className="main">
        {page === "upload" && (
          <Upload
            setAnalysisResult={setAnalysisResult}
            setRoadmapResult={setRoadmapResult}
            setPage={setPage}
          />
        )}
        {page === "dashboard" && analysisResult && (
          <Dashboard result={analysisResult} setPage={setPage} />
        )}
        {page === "roadmap" && roadmapResult && (
          <Roadmap result={roadmapResult} />
        )}
      </main>
    </div>
  )
}

export default App