
import os

from dotenv import load_dotenv
from google import genai


load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_insight(
    temperature_avg,
    temperature_min,
    temperature_max,
    weight_avg,
    weight_min,
    weight_max
):
    prompt = f"""
You are analyzing sensor data.

Temperature:
Average: {temperature_avg}
Minimum: {temperature_min}
Maximum: {temperature_max}

Weight:
Average: {weight_avg}
Minimum: {weight_min}
Maximum: {weight_max}

Give a short plain-English insight about these sensor readings.
Explain whether the values appear relatively stable or variable.
Do not use technical jargon.
Keep the answer to 2 or 3 sentences.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text

