-- URL Snapshot Service

A containerized microservice project designed to demonstrate real DevOps fundamentals: Docker, Docker Compose, service networking, environment variables, database initialization, and clean modular service design.

The system provides two core capabilities:

  1. Scrape and store the HTML of any URL.

  2. Expose the stored snapshots via an API.

Everything runs locally through Docker Compose.

------------------------------------------------------------------------------------------------
-- Components

scraper-service (Python + Flask):

Accepts a URL, fetches the HTML, saves it in the database.

api-service (Node.js + Express):

Serves the stored snapshots over a REST API.

postgres (PostgreSQL 15):

Persists snapshot data. Initialized automatically with schema.

------------------------------------------------------------------------------------------------
-- Tech Stack

Docker

Docker Compose

Python 3.10

Node.js 18

PostgreSQL 15

------------------------------------------------------------------------------------------------
-- Running the Project

1. Clone the repository:

    git clone github.com/flonitoo/url-snapshot-service
   
    cd url-snapshot-service

3. Start the stack:

    docker-compose up --build

This launches:

scraper-service → http://localhost:5001

api-service → http://localhost:5000

postgres → internal network only

------------------------------------------------------------------------------------------------
-- How to Use

Create a snapshot:

curl -X POST http://localhost:5001/scrape \
  -H "Content-Type: application/json" \
  -d '{"url":"https://example.com"}'

Retrieve snapshots:

curl http://localhost:5000/snapshots

------------------------------------------------------------------------------------------------
-- Environment Variables

DB_HOST=postgres

DB_USER=user

DB_PASS=pass

DB_NAME=snapshots
