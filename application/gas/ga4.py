import re
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlencode
import json
import requests
import pandas as pd
from datetime import datetime
import feedparser

def q4_1(question: str = None, file_path: str = None):
    pn = re.search(r'page number (\d+)', question).group(1)
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    soup = BeautifulSoup(requests.get(f'https://stats.espncricinfo.com/stats/engine/stats/index.html?class=2;page={pn};template=results;type=batting', headers=headers).content, 'html.parser')
    zeros = soup.select('tr.data1 > td:nth-child(13)')

    sumz = 0
    for z in zeros:
        sumz += int(z.text.strip())
    return f"{sumz}"

def q4_2(question: str = None, file_path: str = None):
    bounds = re.search('between (\d+) and (\d+)', question)
    lb = min(int(bounds.group(1)), int(bounds.group(2)))
    ub = max(int(bounds.group(1)), int(bounds.group(2)))
    print(lb, ub)
    imdbheaders = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://www.imdb.com/",
    }

    soup = BeautifulSoup(requests.get(f'https://www.imdb.com/search/title/?user_rating={lb},{ub}', headers=imdbheaders).content, 'html.parser')
    titles = soup.select('.ipc-metadata-list-summary-item > div > div > div > div:nth-child(1) > div:nth-child(2)')
    resp = []
    import json
    for t in titles:
        curr = {}
        nameandhref = t.find('a', class_='ipc-title-link-wrapper')
        year = t.select('div:nth-child(2) > span:nth-child(1)')[0].text
        rating = t.find('span', class_='ipc-rating-star--rating').text
        curr["id"] = f"{nameandhref.get('href').split('/')[2]}"
        title = nameandhref.text
        curr["title"] = f"{title}"
        curr["year"] = f"{year}"
        curr["rating"] = f"{rating}"
        resp.append(curr)

    return json.dumps(resp)

def q4_3(question: str = None, file_path: str = None):
    return "http://127.0.0.1:8000/api/p2ga4q3"

def get_wikipedia_url(country: str) -> str:
    """
    Given a country name, returns the Wikipedia URL for the country.
    """
    return f"https://en.wikipedia.org/wiki/{country}"

def extract_headings_from_html(html: str) -> list:
    """
    Extract all headings (H1 to H6) from the given HTML and return a list.
    """
    soup = BeautifulSoup(html, "html.parser")
    headings = []

    # Loop through all the heading tags (H1 to H6)
    for level in range(1, 7):
        for tag in soup.find_all(f'h{level}'):
            headings.append((level, tag.get_text(strip=True)))

    return headings

def generate_markdown_outline(headings: list) -> str:
    """
    Converts the extracted headings into a markdown-formatted outline.
    """
    markdown_outline = "## Contents\n\n"
    for level, heading in headings:
        markdown_outline += "#" * level + f" {heading}\n\n"
    return markdown_outline

def q4_4(question: str = None, file_path: str = None):
    required_city = re.search(r'forecast.*for (\w+)', question).group(1)
    location_url = 'https://locator-service.api.bbci.co.uk/locations?' + urlencode({
        'api_key': 'AGbFAKx58hyjQScCXIYrxuEwJh2W2cmv',
        's': required_city,
        'stack': 'aws',
        'locale': 'en',
        'filter': 'international',
        'place-types': 'settlement,airport,district',
        'order': 'importance',
        'a': 'true',
        'format': 'json'
    })

    # Fetch location data
    result = requests.get(location_url).json()
    weather_url = 'https://www.bbc.com/weather/' + result['response']['results']['results'][0]['id']

    # Fetch weather data
    response = requests.get(weather_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    daily_summary = soup.find('div', attrs={'class': 'wr-day-summary'})
    daily_summary_list = re.findall('[a-zA-Z][^A-Z]*', daily_summary.text)


    # Generate date list
    datelist = pd.date_range(datetime.today(), periods=len(daily_summary_list)).tolist()
    datelist = [date.date().strftime('%Y-%m-%d') for date in datelist]


    # Map dates to descriptions
    weather_data = {date: desc for date, desc in zip(datelist, daily_summary_list)}

    # Convert to JSON
    weather_json = json.dumps(weather_data, indent=4)

    return weather_json

def q4_5(question: str = None, file_path: str = None):
    print('entered ga4q5')
    s = re.search('What is the (maximum|minimum) (latitude|longitude) of the bounding box of the city ([\w\s]+) in the country ([\w\s]+) on the Nominatim API?', question)
    print('maxminlatlong')
    minmax = s.group(1).strip()
    latlong = s.group(2).strip()
    #citycountry = re.search('city (\w+).*country (\w+)', question)
    city = s.group(3).strip()
    country = s.group(4).strip()
    print(minmax, latlong, city, country, sep='\n')
    # import the required library
    from geopy.geocoders import Nominatim

    # Activate the Nominatim geocoder
    locator = Nominatim(user_agent="myGeocoder")

    # Geocode the city Mexico City in Mexico
    location = locator.geocode(f"{city}, {country}")

    # Check if the location was found
    if location:
        # Retrieve the bounding box
        bounding_box = location.raw.get('boundingbox', [])
        print(bounding_box)
        # Check if the bounding box is available
        if len(bounding_box) > 1:
            # Extract the minimum latitude from the bounding box (the first value in the list)
            if (minmax == 'maximum'):
                if (latlong == 'latitude'):
                    ans = bounding_box[1]
                else:
                    ans = bounding_box[3]
            else:
                if (latlong == 'latitude'):
                    ans = bounding_box[0]
                else:
                    ans = bounding_box[2]
            print(f"The {minmax} {latlong} of the bounding box for {city}, {country} is: {ans}")
        else:
            return "Bounding box information not available."
    else:
        return "Location not found."

    return f"{ans}"

def q4_6(question: str = None, file_path: str = None):
    topic = re.search('mentioning ([\w\s]+) (and)? having', question).group(1).strip()
    minpoints = re.search('at least (\d+) points', question).group(1).strip()
    print(topic, minpoints)
    # Fetch the feed with posts mentioning "topic" and having at least minpoints points
    feed_url = "https://hnrss.org/newest?" + urlencode({"q": topic, "points": minpoints})
    print('here')
    feed = feedparser.parse(feed_url)

    # Extract the link of the latest post
    if feed.entries:
        print(feed.entries[0].link)
        return f"{feed.entries[0].link}"

def q4_7(question: str = None, file_path: str = None):
    return "ga4_q7"

def q4_8(question: str = None, file_path: str = None):
    return "https://github.com/22f3000819/tds-ga2-q6"

def q4_9(question: str = None, file_path: str = None):
    import os
    os.environ['JAVA_HOME'] = 'C:\Java\jdk-1.8\bin'
    import tabula
    import pandas as pd
    params = re.search('the total ([\w\s]+) marks of students who scored ([\d.]+) or more marks in ([\w\s]+) in groups (\d+)-(\d+) (including both groups)?', question)
    msub = params.group(1).strip()
    minmarks = int(params.group(2).strip())
    psub = params.group(3).strip()
    lg = int(params.group(4).strip())
    ug = int(params.group(5).strip())
    print(msub, minmarks, psub, lg, ug)
    # Path to the PDF file
    pdf_path = file_path

    # Extract tables from the PDF, specifying pages and multiple_tables=True
    tables = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)

    # Initialize an empty list to store all DataFrames
    all_dfs = []

    # Iterate through each table and add a "Group" column based on the page number
    for i, table in enumerate(tables):
        # Add a "Group" column to the table
        table["Group"] = i + 1  # Group 1 for Page 1, Group 2 for Page 2, etc.
        # Append the table to the list
        all_dfs.append(table)

    # Combine all DataFrames into a single DataFrame
    df = pd.concat(all_dfs, ignore_index=True)

    # Rename columns for easier access (if necessary)
    df.columns = ["Maths", "Physics", "English", "Economics", "Biology", "Group"]

    # Convert marks to numerical data types
    df["Maths"] = pd.to_numeric(df["Maths"], errors="coerce")
    df["Physics"] = pd.to_numeric(df["Physics"], errors="coerce")
    df["English"] = pd.to_numeric(df["English"], errors="coerce")
    df["Economics"] = pd.to_numeric(df["Economics"], errors="coerce")
    df["Biology"] = pd.to_numeric(df["Biology"], errors="coerce")
    df["Group"] = pd.to_numeric(df["Group"], errors="coerce")

    # Drop rows with missing values (if any)
    df.dropna(inplace=True)

    # Display the first few rows of the combined DataFrame
    print(df.head())

    # Display the data types of the columns
    print(df.dtypes)
    filtered_df = df[(df[psub] >= minmarks) & (df["Group"].between(lg, ug))]

    total_subj_marks = filtered_df[msub].sum()
    print(total_subj_marks)
    return f"{total_subj_marks}"

def q4_10(question: str = None, file_path: str = None):
    return "ga4_q10"