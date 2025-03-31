import httpx
import json
import subprocess
import hashlib
import re
import os
import zipfile
import pandas as pd
import chardet
import numpy as np
from datetime import timedelta
from datetime import datetime
import platform
from bs4 import BeautifulSoup
from urllib.parse import urlencode

def q1_1():
    return "Version: Code 1.98.2 OS Version: Windows_NT x64 10.0.22631"

def q1_2(email, **kwargs):
    print('q1_2')
    r = httpx.get('https://httpbin.org/get?'+urlencode({'email': '22f3000819@ds.study.iitm.ac.in'}))
    js = json.loads(r.text)

    resp = {}
    for key, val in js.items():
        if key == "headers":
            val["User-Agent"] = "HTTPie/3.2.1"
        resp[key] = val
    print('resp')
    resp_json_string = json.dumps(resp)
    print('resp_json_string')
    return f"{resp_json_string}"

def q1_3(temp_file_path):
    process = subprocess.run(
        ["npx", "-y", "prettier@3.4.2", temp_file_path], 
        capture_output=True, text=True, shell=True
    )

    # Compute SHA-256 hash of the output
    sha256_hash = hashlib.sha256(process.stdout.encode()).hexdigest()
    return f"{sha256_hash}"

def q1_4(question):
    # Extract numbers from the sentence
    numbers = list(map(int, re.findall(r'\d+', question)))

    if len(numbers) >= 4:
        rows, cols, start, step, row_limit, col_limit = *numbers[:4], *numbers[4:6]

        # Generate the sequence
        sequence = [[start + (i * step) for i in range(cols)] for _ in range(rows)]

        # Apply ARRAY_CONSTRAIN to get the first 'row_limit' rows and 'col_limit' columns
        constrained_array = [row[:col_limit] for row in sequence[:row_limit]]

        # Compute the sum
        result = sum(constrained_array[0])

        return f"{result}"
    else:
        return "Not enough numbers to process."

def q1_5(question):
    # Extract numbers inside curly braces
    array_matches = re.findall(r'\{([\d, ]+)\}', question)

    if len(array_matches) >= 2:
        main_array = list(map(int, array_matches[0].split(',')))
        sort_by_array = list(map(int, array_matches[1].split(',')))

        # Extract the two numbers at the end of TAKE function
        take_numbers = re.findall(r'TAKE\(.*?,\s*(\d+),\s*(\d+)\)', question)
        if take_numbers:
            take_row, take_cols = map(int, take_numbers[0])

            # Perform SORTBY operation
            sorted_array = [x for _, x in sorted(zip(sort_by_array, main_array))]

            # Perform TAKE operation (first `take_cols` elements from row `take_row`, which is 1-based)
            result_array = sorted_array[:take_cols]

            # Compute the SUM
            result = sum(result_array)
            return f"{result}"
        else:
            return "TAKE function numbers not found."
    else:
        return "Arrays not found in text."

def q1_6(question: str, html_file_path: str) -> str:
    with open(html_file_path, 'r') as htmlfile:
        soup = BeautifulSoup(htmlfile, 'html.parser')
    return f"{soup.find('input',type='hidden').get('value')}"

def q1_7(question, **kwargs):

    # Extract the day and dates using regex
    match = re.search(r'How many (\w+)s? .*? (\d{4}-\d{2}-\d{2}) to (\d{4}-\d{2}-\d{2})\?', question)

    if match:
        day_name = match.group(1)  # "Wednesday"
        start_date = datetime.strptime(match.group(2), "%Y-%m-%d")
        end_date = datetime.strptime(match.group(3), "%Y-%m-%d")
    else:
        return "Invalid input format"

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

    return f"{count}"

def q1_8(question: str, zip_file_path: str):
    column_match = re.search(r'"(.+)"', question)
    if not column_match:
        raise ValueError("Column name not found in the question.")
    column_name = column_match.group(1)
    print(column_name)
    # Extract the zip file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        extracted_dir = os.path.dirname(zip_file_path)  # Extract in the same directory
        zip_ref.extractall(extracted_dir)
        extracted_files = zip_ref.namelist()
    
    extracted_csv_path = None
    for file in extracted_files:
        if file.endswith(".csv"):
            extracted_csv_path = os.path.join(extracted_dir, file)
            break
        
    if extracted_csv_path is None:
        raise FileNotFoundError("No CSV file found in the extracted ZIP.")
    print("extracted dir", extracted_dir)
    print(extracted_csv_path)

    # Read CSV and extract the answer column
    df = pd.read_csv(extracted_csv_path)
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in the CSV file.")

    # Return the value in the specified column (assuming a single row)
    return f"{df[column_name].iloc[0]}"

def q1_9(question: str):
    # Extract JSON from the question
    json_match = re.search(r'\[\{.*\}\]', question)
    print('json_match')
    if not json_match:
        raise ValueError("JSON data not found in the question.")
    
    json_data = json.loads(json_match.group())  # Parse JSON
    print('json_data')
    # Sort by age first, then by name in case of ties
    sorted_json = sorted(json_data, key=lambda x: (x["age"], x["name"]))
    print('sorted_json')
    # Return JSON as a compact string (no spaces or newlines)
    json_str = json.dumps(sorted_json)
    return f"{json_str}"

def q1_10(question: str, file_path: str) -> str:
    # Read the txt file and convert it into a dictionary
    with open(file_path, 'r', encoding='utf-8') as f:
        data = dict(line.strip().split('=') for line in f if '=' in line)

    # Convert the dictionary to JSON (ensuring the structure is correct)
    json_str = json.dumps(data, separators=(',', ':'))  # Compact JSON

    # Step 2: Try different hash functions
    hash_sha256 = hashlib.sha256(json_str.encode()).hexdigest()

    return f"{hash_sha256}"  # Returning SHA-256 by default

def q1_11(question: str, html_file_path: str) -> str:
    with open(html_file_path, 'r') as htmlfile:
        soup = BeautifulSoup(htmlfile, 'html.parser')

    foo = soup.select('div.d-none')[0].select('.foo')
    s = 0
    for f in foo:
        s += int(f.get('data-value'))
    return f"{s}"

def q1_12(question: str, zip_file_path: str) -> int:
    # Dynamically extract symbols from the question
    symbols = re.findall(r'(.) OR', question)  # More general regex for extracting symbols
    symbols.append(re.findall(r'OR (.)', question)[-1])
    # Extract ZIP file
    extracted_dir = os.path.splitext(zip_file_path)[0]  # Extract to the same directory
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extracted_dir)

    total_sum = 0

    # Process each file in the extracted directory
    for file_name in os.listdir(extracted_dir):
        file_path = os.path.join(extracted_dir, file_name)

        # Detect encoding
        with open(file_path, 'rb') as f:
            raw_data = f.read()
            detected_encoding = chardet.detect(raw_data)['encoding']

        # Determine delimiter based on file type
        delimiter = ',' if file_name.endswith('.csv') else '\t'

        # Read file with detected encoding
        try:
            df = pd.read_csv(file_path, encoding=detected_encoding, delimiter=delimiter)
        except Exception as e:
            print(f"Error reading {file_name} with {detected_encoding}: {e}")
            continue

        # Normalize column names
        df.columns = df.columns.str.strip().str.lower()

        # Ensure required columns exist
        if 'symbol' in df.columns and 'value' in df.columns:
            total_sum += df[df['symbol'].isin(symbols)]['value'].sum()

    return f"{total_sum}"

def q1_13(question: str):
    return "https://raw.githubusercontent.com/22f3000819/tds_p2_ga1_13/main/email.json"

def q1_14(question: str, zip_file_path: str) -> str:
    # Step 1: Extract the zip file into a new folder
    extract_dir = os.path.splitext(zip_file_path)[0]  # Extracted folder name
    os.makedirs(extract_dir, exist_ok=True)

    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)

    # Step 2: Iterate through each file and replace "IITM" (case-insensitive) with "IIT Madras"
    pattern = re.compile(r'IITM', re.IGNORECASE)

    for root, _, files in os.walk(extract_dir):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            # Read the file in binary mode to preserve line endings
            with open(file_path, 'rb') as f:
                content = f.read()

            # Decode content while keeping encoding intact
            original_encoding = None
            for encoding in ['utf-8', 'latin-1', 'utf-16']:
                try:
                    text = content.decode(encoding)
                    original_encoding = encoding
                    break
                except UnicodeDecodeError:
                    continue
            
            if original_encoding is None:
                raise ValueError(f"Could not determine encoding for {file_name}")

            # Replace all occurrences of "IITM" in a case-insensitive manner
            updated_text = pattern.sub("IIT Madras", text)

            # Write back the modified content using the original encoding
            with open(file_path, 'wb') as f:
                f.write(updated_text.encode(original_encoding))

    # Step 3: Compute SHA-256 hash equivalent to `cat * | sha256sum`
    sha256_hash = hashlib.sha256()

    for root, _, files in os.walk(extract_dir):
        for file_name in sorted(files):  # Sorting ensures consistent hashing
            file_path = os.path.join(root, file_name)

            with open(file_path, 'rb') as f:
                while chunk := f.read(8192):  # Read in chunks
                    sha256_hash.update(chunk)

    return f"{sha256_hash.hexdigest()}"


def q1_15(question: str, zip_file_path: str) -> int:
    # Step 1: Extract required parameters from the question
    size_match = re.search(r"at least (\d+) bytes", question)
    date_match = re.search(r"on or after (\w{3}, \d{1,2} \w{3}, \d{4}, [\d:]+ [aApPmM]{2} IST)", question)

    if not size_match or not date_match:
        raise ValueError("Could not extract size or date from the question.")

    min_size = int(size_match.group(1))
    date_str = date_match.group(1)

    # Convert given date to a comparable timestamp
    reference_datetime = datetime.strptime(date_str, "%a, %d %b, %Y, %I:%M %p IST")
    # Step 2: Extract the zip file while preserving timestamps
    extract_dir = os.path.splitext(zip_file_path)[0]  # Extracted folder name
    os.makedirs(extract_dir, exist_ok=True)
    system_os = platform.system()
    if system_os == "Windows":
        subprocess.run(["7z", "x", zip_file_path, f"-o{os.path.abspath(extract_dir)}"], check=True, shell=True)
    else:
        subprocess.run(["unzip", "-o", zip_file_path, "-d", extract_dir], check=True)
    # Step 3: Iterate over files and compute total size
    total_size = 0

    for root, _, files in os.walk(extract_dir):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            # Get file size
            file_size = os.path.getsize(file_path)

            # Get modification time
            mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            # Check if file meets the conditions
            if file_size >= min_size and mod_time >= reference_datetime:
                print(file_size, mod_time)
                total_size += file_size

    return f"{total_size}"


def q1_16(question: str, zip_file_path: str):
    process = subprocess.run(["./q16script.sh", zip_file_path], capture_output=True, text=True)
    return f"{process.stdout}"

def q1_17(question: str, zip_file_path: str) -> int:
    extract_dir = os.path.splitext(zip_file_path)[0]  # Extracted folder name
    os.makedirs(extract_dir, exist_ok=True)

    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    
    file_path = []
    for root, _, files in os.walk(extract_dir):
        for file_name in files:
            file_path.append(os.path.join(root, file_name))
    with open(file_path[0], "r") as f:
        lines_a = set(f.readlines())

    with open(file_path[1], "r") as f:
        lines_b = set(f.readlines())

    # Find lines present in file_a but not in file_b
    unique_lines = lines_a - lines_b
    return f"{len(unique_lines)}"

def q1_18(question: str, zip_file_path: str = None):
    return "SELECT SUM(units * price) FROM tickets WHERE LOWER(TRIM(type)) = 'gold';"