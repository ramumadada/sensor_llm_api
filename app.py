
from flask import Flask, jsonify

from database import create_table, get_readings, get_statistics
from llm import generate_insight


app = Flask(__name__)

create_table()


@app.route("/readings", methods=["GET"])
def readings():
    data = get_readings()

    return jsonify({
        "count": len(data),
        "readings": data
    })


@app.route("/insight", methods=["GET"])
def insight():
    stats = get_statistics()

    if stats is None:
        return jsonify({
            "error": "No sensor readings available"
        }), 404

    result = generate_insight(
        stats["temperature_avg"],
        stats["temperature_min"],
        stats["temperature_max"],
        stats["weight_avg"],
        stats["weight_min"],
        stats["weight_max"]
    )

    return jsonify({
        "statistics": stats,
        "insight": result
    })


if __name__ == "__main__":
    app.run(debug=True)

