import pandas as pd
import numpy as np
from datetime import datetime
import re
import os
import gzip
import json
from collections import defaultdict
from fuzzywuzzy import fuzz

def convert_to_datetime(date):
    for fmt in ("%m-%d-%Y", "%Y/%m/%d", "%Y-%m-%d"):
        try:
            return datetime.strptime(str(date), fmt)
        except ValueError:
            continue
    return pd.NaT
def q5_1(question: str = None, file_path: str = None):
    s = re.search('before ([^.,;]+) for (\w+) sold in (\w+)', question)
    datetime_string = s.group(1)
    mdy = re.search(r'(\w{3}) (\d{1,2}) (\d{4}) (\d{1,2}:\d{1,2}:\d{1,2})', datetime_string)
    month = mdy.group(1)
    date = mdy.group(2)
    year = mdy.group(3)
    time = mdy.group(4)
    print(month, date, year, time)
    product = s.group(2)
    country = s.group(3)
    print(product, country)
    # Step 2: Load Data
    try:
        df = pd.read_excel(file_path)
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return f"Error reading Excel file: {e}"
    print("read_excel")
    # Step 3: Trim and Normalize Country Names
    df['Country'] = df['Country'].str.strip().str.upper()  # Remove spaces and convert to uppercase
    print('trimmed and normalized')
    # Step 4: Standardize Country Names
    country_mapping = {
        "USA": "US", 
        "U.S.A": "US", 
        "United States": "US", 
        "UNITED STATES": "US",
        "US": "US",
        "BRA": "BR", 
        "Brazil": "BR", 
        "BRAZIL": "BR",
        "Bra": "BR",
        "U.K": "UK", 
        "UK": "UK", 
        "United Kingdom": "UK",
        "UNITED KINGDOM": "UK",
        "Fra": "FR", 
        "FRA": "FR", 
        "France": "FR",
        "FRANCE": "FR",
        "India": "IN", 
        "INDIA": "IN",
        "IND": "IN", 
        "Ind": "IN",
        "UAE": "AE", 
        "U.A.E": "AE", 
        "United Arab Emirates": "AE", 
        "UNITED ARAB EMIRATES": "AE",
        "AE": "AE"
    }
    df['Country'] = df['Country'].replace(country_mapping)
    print(df['Country'].unique())
    # Step 5: Standardize Date Formats

    df['Date'] = df['Date'].apply(convert_to_datetime)
    print('date standardised')
    # Step 6: Extract Product Name (Before "/")
    df['Product/Code'] = df['Product/Code'].str.split('/').str[0].str.strip()
    print('product extracted')
    # Step 7: Clean and Convert Sales & Cost Columns
    df['Sales'] = df['Sales'].astype(str).str.replace("USD", "").str.strip().astype(float)
    df['Cost'] = df['Cost'].astype(str).str.replace("USD", "").str.strip()
    print('cleaned sales and cost')
    # Handle missing cost values (assume 50% of Sales)
    df['Cost'] = pd.to_numeric(df['Cost'], errors='coerce')
    df.loc[df['Cost'].isna(), 'Cost'] = df['Sales'] * 0.5
    print('handled missing cost')
    # Step 8: Apply Filters
    date_filter = datetime.strptime(f"{month} {date} {year} {time}", "%b %d %Y %H:%M:%S")  # Tue Jan 03 2023 16:56:57 GMT+0530
    df_filtered = df[
        (df['Date'] <= date_filter) &
        (df['Product/Code'].str.lower() == product.lower()) &
        (df['Country'] == country)
    ]

    # Step 9: Calculate Total Margin
    total_sales = df_filtered['Sales'].sum()
    total_cost = df_filtered['Cost'].sum()

    if total_sales > 0:
        total_margin = (total_sales - total_cost) / total_sales
    else:
        total_margin = 0

    # Step 10: Display Results
    print(f"Total Sales: {total_sales:.2f}")
    print(f"Total Cost: {total_cost:.2f}")
    print(f"Total Margin: {total_margin:.4f}")

    return f"{total_margin:.4f}"



def q5_2(question: str = None, file_path: str = None):
    # Data Extraction: Read file line by line and extract student IDs
    student_ids = set()
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            matches = re.findall(r'\b[A-Z0-9]{10}\b', line)  # Match exact 10-character alphanumeric IDs
            student_ids.update(matches)

    # Reporting: Count the number of unique student IDs
    print(f"Number of unique students: {len(student_ids)}")
    return f"{len(student_ids)}"

def q5_3(question: str = None, file_path: str = None):
    return "ga5_q3"


def parse_log_line(line):
    log_pattern = (r'^(\S+) (\S+) (\S+) \[(.*?)\] "(\S+) (.*?) (\S+)" (\d+) (\S+) "(.*?)" "(.*?)" (\S+) (\S+)$')
    match = re.match(log_pattern, line)
    if match:
        return {
            "ip": match.group(1),
            "time": match.group(4),
            "method": match.group(5),
            "url": match.group(6),
            "protocol": match.group(7),
            "status": int(match.group(8)),
            "size": int(match.group(9)) if match.group(9).isdigit() else 0,
            "referer": match.group(10),
            "user_agent": match.group(11),
            "vhost": match.group(12),
            "server": match.group(13)
        }
    return None

# Load and parse the log file
def load_logs(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return pd.DataFrame()

    parsed_logs = []
    with gzip.open(file_path, 'rt', encoding='utf-8') as f:
        for line in f:
            parsed_entry = parse_log_line(line)
            if parsed_entry:
                parsed_logs.append(parsed_entry)
    return pd.DataFrame(parsed_logs)

# Convert time format
def convert_time(timestamp):
    return datetime.strptime(timestamp, "%d/%b/%Y:%H:%M:%S %z")

def q5_4(question: str = None, file_path: str = None):
    df = load_logs('s-anand.net-May-2024.gz')
    s = re.search('under ([/\w]+) on ([\d-]+),', question)
    under = s.group(1).strip(' ')
    on = s.group(2).strip(' ')
    print(s.group(1).strip(' '))
    print(s.group(2).strip(' '))
    if not df.empty:
        print('if')
        df["datetime"] = df["time"].apply(convert_time)
        print('converted datetime')
        df["date"] = df["datetime"].dt.strftime('%Y-%m-%d')
        print('converted date')

        # Filter conditions for /hindimp3/ on 2024-05-16
        filtered_df = df[
            (df["url"].str.contains(under)) &
            (df["date"] == on)
        ]
        print(filtered_df.head())
        # Aggregate data by IP
        ip_data = filtered_df.groupby("ip")["size"].sum().reset_index()
        print('aggregated')
        # Identify the top data consumer
        try:
            top_ip = ip_data.loc[ip_data["size"].idxmax()]
        except Exception as e:
            return f"Error: {e}"
        print('top ip')
        # Output the result
        print(f"Top IP Address: {top_ip['ip']}")
        print(f"Total Bytes Downloaded: {top_ip['size']}")
    else:
        return "No log data available for processing."
    return f"{top_ip['size']}"

def get_city_clusters(data, target_city, threshold=80):
    """Group city names that are likely misspellings of the target city."""
    clusters = defaultdict(list)
    unique_cities = set(entry['city'] for entry in data)
    
    for city in unique_cities:
        similarity = fuzz.ratio(target_city.lower(), city.lower())
        if similarity >= threshold:
            clusters[target_city].append(city)
    
    return clusters

def calculate_fish_sales_for_city(data, target_city, product, min_sales):
    """Calculate total Fish sales for a city (including misspellings)."""
    clusters = get_city_clusters(data, target_city)
    if not clusters:
        return 0  # No matching city found
    
    # Get all variations of the target city
    city_variations = clusters[target_city]
    
    # Filter entries: product is Fish and sales >= min_sales
    filtered_data = [
        entry for entry in data 
        if entry['product'] == product 
        and entry['sales'] >= min_sales
        and entry['city'] in city_variations
    ]
    
    # Sum the sales
    total_sales = sum(entry['sales'] for entry in filtered_data)
    return total_sales

def q5_5(question: str = None, file_path: str = None):
    print('q5_5')
    # Load the data
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Example usage: Calculate for "Dhaka"
    product = re.search(r'units of ([\w\s]+) were', question).group(1).strip()
    target_city = re.search(r'sold in ([\w\s]+) on', question).group(1).strip()
    minsales = int(re.search(r'with at least (\d+) units', question).group(1).strip())
    total_sales = calculate_fish_sales_for_city(data, target_city, product, minsales)
    print(f"Total units of {product} sold in {target_city} (including misspellings) with at least {minsales} units: {total_sales}")
    return f"{total_sales}"


def q5_6(question: str = None, file_path: str = None):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    tot = 0
    for line in lines:
        try:
            saleval = re.search(r'"\s*sales\s*"\s*:\s*(\d+)', line).group(1)
        except:
            saleval = 0
        tot += int(saleval)
    return f"{tot}"

def q5_7(question: str = None, file_path: str = None):
    return "ga5_q7"

def q5_8(question: str = None, file_path: str = None):
    return "ga5_q8"

def q5_9(question: str = None, file_path: str = None):
    return "ga5_q9"

def q5_10(question: str = None, file_path: str = None):
    return "ga5_q10"