export default function Roadmap({ result }) {
  return (
    <div className="card">
      <h2>Your Learning Roadmap</h2>
      <p style={{ color: "#555", marginBottom: "1.5rem" }}>
        Here are the recommended steps to bridge your skill gaps:
      </p>
      {result.steps && result.steps.map((step, i) => (
        <div key={i} className="roadmap-step">
          <h4>Step {i + 1}: {step.skill}</h4>
          <p>{step.resource}</p>
          <p style={{ marginTop: "0.3rem" }}>
            ⏱ {step.duration} &nbsp;
            {step.free && <span className="free-badge">Free</span>}
          </p>
        </div>
      ))}
    </div>
  )
}