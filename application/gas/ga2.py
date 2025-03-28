from PIL import Image
from io import BytesIO
import hashlib
import re
import numpy as np
import colorsys

def q2_1(question: str = None, file_path: str = None):
    return """# Step Analysis Report

        ## Introduction
        Tracking daily steps is an **important** aspect of maintaining an active lifestyle. This analysis examines the number of steps walked each day over a week and compares the results over time and with friends.

        ## Methodology
        The data was collected using a fitness tracker and recorded daily. The following steps were taken:

        1. Recorded step counts for a week.
        2. Compared daily steps with previous weeks.
        3. Compared steps with friends to analyze trends.

        ## Data Collection
        - Steps were tracked using a fitness device.
        - Data was logged into a spreadsheet.
        - Weekly trends were calculated.

        ## Weekly Step Count
        | Day       | Steps Walked |
        |-----------|-------------|
        | Monday    | 8,500       |
        | Tuesday   | 9,200       |
        | Wednesday | 7,800       |
        | Thursday  | 10,000      |
        | Friday    | 9,600       |
        | Saturday  | 11,500      |
        | Sunday    | 12,000      |

        ## Code for Step Analysis
        To analyze the step data, we used Python:
        ```python
        import pandas as pd

        data = {'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
                'Steps': [8500, 9200, 7800, 10000, 9600, 11500, 12000]}

        df = pd.DataFrame(data)
        print(df.describe())
        ```

        ## Observations
        - *Tuesday* had a slightly higher step count than *Monday*.
        - The highest step count was recorded on **Sunday**.
        - There was a general increase in steps toward the weekend.

        ## Comparison with Friends
        > "Walking together keeps us motivated!" – A friend from the study group

        Here’s how my steps compared to my friends:

        - Alice: **10,500** steps/day average
        - Bob: **9,800** steps/day average
        - Me: **9,800** steps/day average

        ## Further Improvements
        Some ways to improve step count tracking:

        - **Increase daily goals** to 12,000 steps.
        - *Use a reminder app* to stay active throughout the day.
        - Track steps using an advanced fitness tracker.

        ## Reference
        For more on step tracking, visit [Healthline](https://www.healthline.com/health/how-many-steps-a-day)

        ## Visualization
        ![Step Count Graph](https://example.com/step-count-graph.jpg)
    """

def q2_2(question: str = None, file_path: str = None):
    image = Image.open(file_path)
    img_io = BytesIO()
    image.save(img_io, format="WEBP", lossless=True, quality=100)
    img_io.seek(0)
    
    return img_io

def q2_3(question: str = None, file_path: str = None):
    return "ga2_q3"

def q2_4(question: str = None, file_path: str = None):
    email = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', question).group(0)
    return hashlib.sha256(f"{email} {2025}".encode()).hexdigest()[-5:]

def q2_5(question: str = None, file_path: str = None):
    l = re.search(r'lightness > ([\d\.]+)', question).group(1)
    image = Image.open(file_path)

    rgb = np.array(image) / 255.0
    lightness = np.apply_along_axis(lambda x: colorsys.rgb_to_hls(*x)[1], 2, rgb)
    light_pixels = np.sum(lightness > float(l))
    return f'{light_pixels}'

def q2_6(question: str = None, file_path: str = None):
    return "ga2_q6"

def q2_7(question: str = None, file_path: str = None):
    return "ga2_q7"

def q2_8(question: str = None, file_path: str = None):
    return "ga2_q8"

def q2_9(question: str = None, file_path: str = None):
    return "ga2_q9"

def q2_10(question: str = None, file_path: str = None):
    return "https://llama-pi.vercel.app/"