from flask import Flask, request, jsonify
import requests
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")

def get_conn():
    return psycopg2.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        dbname=DB_NAME
    )

@app.route("/scrape", methods=["POST"])
def scrape():
    data = request.get_json()
    url = data.get("url")

    html = requests.get(url).text

    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO snapshots(url, html) VALUES (%s, %s)", (url, html))
    conn.commit()
    cur.close()
    conn.close()

    return {"status": "saved"}
