import sqlite3
from pathlib import Path

DB_PATH = Path("data/sensor.db")


def get_connection():
    DB_PATH.parent.mkdir(exist_ok=True)
    return sqlite3.connect(DB_PATH)


def create_table():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS sensor_readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            temperature REAL NOT NULL,
            weight REAL NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def save_reading(reading):
    conn = get_connection()

    conn.execute(
        """
        INSERT INTO sensor_readings
        (timestamp, temperature, weight)
        VALUES (?, ?, ?)
        """,
        (
            reading["timestamp"],
            reading["temperature"],
            reading["weight"],
        ),
    )

    conn.commit()
    conn.close()


def get_readings():
    conn = get_connection()

    rows = conn.execute(
        """
        SELECT id, timestamp, temperature, weight
        FROM sensor_readings
        ORDER BY id
        """
    ).fetchall()

    conn.close()

    return [
        {
            "id": row[0],
            "timestamp": row[1],
            "temperature": row[2],
            "weight": row[3],
        }
        for row in rows
    ]

def get_statistics():
    conn = get_connection()

    row = conn.execute("""
        SELECT
            AVG(temperature),
            MIN(temperature),
            MAX(temperature),
            AVG(weight),
            MIN(weight),
            MAX(weight)
        FROM sensor_readings
    """).fetchone()

    conn.close()

    if row[0] is None:
        return None

    return {
        "temperature_avg": round(row[0], 2),
        "temperature_min": round(row[1], 2),
        "temperature_max": round(row[2], 2),
        "weight_avg": round(row[3], 2),
        "weight_min": round(row[4], 2),
        "weight_max": round(row[5], 2)
    }
