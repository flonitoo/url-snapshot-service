const express = require("express");
const { Pool } = require("pg");

const app = express();
app.use(express.json());

const pool = new Pool({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASS,
  database: process.env.DB_NAME
});

app.get("/snapshots", async (req, res) => {
  const result = await pool.query("SELECT * FROM snapshots ORDER BY id DESC");
  res.json(result.rows);
});

app.listen(5000, () => console.log("API running on 5000"));
