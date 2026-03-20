import { Radar } from "react-chartjs-2"
import {
  Chart as ChartJS, RadialLinearScale, PointElement,
  LineElement, Filler, Tooltip, Legend
} from "chart.js"

ChartJS.register(RadialLinearScale, PointElement, LineElement, Filler, Tooltip, Legend)

export default function Dashboard({ result, setPage }) {
  const allSkills = [...result.matched_skills, ...result.missing_skills]
  const data = {
    labels: allSkills,
    datasets: [
      {
        label: "Your Skills",
        data: allSkills.map(s => result.matched_skills.includes(s) ? 1 : 0),
        backgroundColor: "rgba(233, 69, 96, 0.2)",
        borderColor: "#e94560",
        pointBackgroundColor: "#e94560",
      }
    ]
  }

  const options = {
    scales: { r: { min: 0, max: 1, ticks: { display: false } } },
    plugins: { legend: { display: false } }
  }

  const scoreColor = result.match_score >= 70 ? "#28a745" : result.match_score >= 40 ? "#ffc107" : "#e94560"

  return (
    <>
      <div className="card">
        <h2>Skill Match for {result.targetRole}</h2>
        <p className="source-badge">Powered by: {result.source === "ai" ? "AI Analysis" : "Rule-based fallback"}</p>
        <div className="score-circle" style={{ background: scoreColor }}>
          {result.match_score}%
        </div>

        <h3>Matched Skills</h3>
        <div className="skills-grid">
          {result.matched_skills.map(s => (
            <span key={s} className="skill-pill matched">{s}</span>
          ))}
        </div>

        <h3 style={{ marginTop: "1rem" }}>Missing Skills</h3>
        <div className="skills-grid">
          {result.missing_skills.map(s => (
            <span key={s} className="skill-pill missing">{s}</span>
          ))}
        </div>
      </div>

      <div className="card">
        <h2>Skill Radar</h2>
        <div style={{ maxWidth: "400px", margin: "0 auto" }}>
          <Radar data={data} options={options} />
        </div>
      </div>

      <button className="btn" onClick={() => setPage("roadmap")}>
        View Learning Roadmap →
      </button>
    </>
  )
}