import React, { useEffect, useState } from "react";
import "./App.css";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend
} from "recharts";

function App() {
  const [logs, setLogs] = useState([]);

  // Auto-refreshing logs every 60 seconds
  useEffect(() => {
    const fetchLogs = () => {
      fetch("https://workpulse-backend.onrender.com/logs") // 🔹 Changed to Render backend URL
        .then((res) => res.json())
        .then((data) => setLogs(data.reverse()))
        .catch((err) => console.error("Error fetching logs:", err));
    };

    fetchLogs(); // Initial load

    const interval = setInterval(fetchLogs, 60000); // Refresh every 60 seconds

    return () => clearInterval(interval); // Cleanup on unmount
  }, []);

  return (
    <div className="App">
      <h2>📊 WorkPulse Dashboard</h2>

      <table>
        <thead>
          <tr>
            <th>Timestamp</th>
            <th>Idle Time (s)</th>
            <th>Active Applications</th>
          </tr>
        </thead>
        <tbody>
          {logs.map((log, index) => (
            <tr key={index}>
              <td>{log.timestamp}</td>
              <td>{log.idle_time ? log.idle_time.toFixed(2) : "0.00"}</td>
              <td>{log.active_apps ? log.active_apps.join(", ") : "N/A"}</td>
            </tr>
          ))}
        </tbody>
      </table>

      {/* Chart below the table */}
      {logs.length > 0 ? (
        <>
          <h3>📈 Idle Time Chart (seconds)</h3>
          <LineChart width={900} height={300} data={logs}>
            <XAxis dataKey="timestamp" />
            <YAxis />
            <CartesianGrid stroke="#ccc" />
            <Tooltip />
            <Legend />
            <Line
              type="monotone"
              dataKey="idle_time"
              stroke="#8884d8"
              strokeWidth={2}
            />
          </LineChart>
        </>
      ) : (
        <p>Loading chart data...</p>
      )}
    </div>
  );
}

export default App;