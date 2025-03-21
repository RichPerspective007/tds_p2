import httpx
import json
import subprocess
import hashlib


def q1():
    return "Version:          Code 1.98.2 (ddc367ed5c8936efe395cffeec279b04ffd7db78, 2025-03-12T13:32:45.399Z)\nOS Version:       Windows_NT x64 10.0.22631"

def q2(email, **kwargs):
    r = httpx.get(f'https://httpbin.org/get?email={email}')
    js = json.loads(r.text)

    resp = {}
    for key, val in js.items():
        if key == "headers":
            val["User-Agent"] = "HTTPie/3.2.1"
        resp[key] = val

    return resp

def q3(temp_file_path):
    process = subprocess.run(
        ["npx", "-y", "prettier@3.4.2", temp_file_path], 
        capture_output=True, text=True, shell=True
    )

    # Compute SHA-256 hash of the output
    sha256_hash = hashlib.sha256(process.stdout.encode()).hexdigest()
    return sha256_hash

def q4():
    import numpy as np

    # Generate a 100x100 sequence starting at 5, with a step of 2
    sequence = np.arange(5, 5 + (100 * 100 * 2), 2).reshape(100, 100)

    # Extract the first row and first 10 columns
    subset = sequence[:1, :10]

    # Compute the sum
    result = np.sum(subset)

    return result

def q7(day_name, start_date, end_date, **kwargs):
    from datetime import timedelta

    if day_name[-1].lower() == 's':
        day_name = day_name[0] + day_name[1:-1].lower() 

    # Convert day name to corresponding weekday number (Monday=0, ..., Sunday=6)
    target_weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].index(day_name)

    # Count Wednesdays in the given date range
    count = 0
    current_date = start_date

    while current_date <= end_date:
        if current_date.weekday() == target_weekday:
            count += 1
        current_date += timedelta(days=1)

    return count

