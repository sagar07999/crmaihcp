import { useEffect, useState } from "react";
import API from "../../services/api";

function StatsCards() {
  const [stats, setStats] = useState({
    total: 0,
    doctors: 0,
    hospitals: 0,
    products: 0,
  });

  useEffect(() => {
    loadStats();
  }, []);

  const loadStats = async () => {
    const res = await API.get("/interactions/");

    const interactions = res.data;

    setStats({
      total: interactions.length,
      doctors: new Set(interactions.map(i => i.doctor_name)).size,
      hospitals: new Set(interactions.map(i => i.hospital)).size,
      products: new Set(interactions.map(i => i.products)).size,
    });
  };

  return (
    <div className="row mb-4">

      <div className="col-md-3">
        <div className="card shadow text-center">
          <div className="card-body">
            <h2>{stats.total}</h2>
            <p>Total Interactions</p>
          </div>
        </div>
      </div>

      <div className="col-md-3">
        <div className="card shadow text-center">
          <div className="card-body">
            <h2>{stats.doctors}</h2>
            <p>Doctors</p>
          </div>
        </div>
      </div>

      <div className="col-md-3">
        <div className="card shadow text-center">
          <div className="card-body">
            <h2>{stats.hospitals}</h2>
            <p>Hospitals</p>
          </div>
        </div>
      </div>

      <div className="col-md-3">
        <div className="card shadow text-center">
          <div className="card-body">
            <h2>{stats.products}</h2>
            <p>Products</p>
          </div>
        </div>
      </div>

    </div>
  );
}

export default StatsCards;