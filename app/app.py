import os
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

DATABASE_URL = os.environ.get("DATABASE_URL")


def get_conn():
    return psycopg2.connect(DATABASE_URL)


@app.route("/")
def index():
    return "Hello from lab2 app!\n"


@app.route("/db-ping")
def db_ping():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "CREATE TABLE IF NOT EXISTS ping ("
                "id SERIAL PRIMARY KEY, ts TIMESTAMPTZ DEFAULT now())"
            )
            cur.execute("INSERT INTO ping DEFAULT VALUES RETURNING id, ts;")
            row = cur.fetchone()
    return jsonify({"id": row[0], "ts": row[1].isoformat()})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
