import random
from datetime import datetime

def generate_reading():
    return {
        "timestamp": datetime.now().isoformat(),
        "temperature": round(random.uniform(25, 35), 2),
        "weight": round(random.uniform(45, 60), 2),
    }

