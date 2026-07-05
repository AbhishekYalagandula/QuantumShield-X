import "./StatsCard.css";

function StatsCard({ title, value, icon }) {
  return (
    <div className="stats-card">

      <div className="icon">{icon}</div>

      <h2>{value}</h2>

      <p>{title}</p>

    </div>
  );
}

export default StatsCard;