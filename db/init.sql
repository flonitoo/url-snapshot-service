CREATE TABLE IF NOT EXISTS snapshots (
    id SERIAL PRIMARY KEY,
    url TEXT,
    html TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
