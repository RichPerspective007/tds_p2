from sentence_transformers import SentenceTransformer, util
import re

from .gas.ga1 import q1, q2, q3, q7

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Your predefined 50 questions
questions = [
    "Install and run Visual Studio Code. In your Terminal (or Command Prompt), type code -s and press Enter. Copy and paste the entire output below. What is the output of code -s?",
    "Running uv run --with httpie -- https [URL] installs the Python package httpie and sends a HTTPS request to the URL. Send a HTTPS request to https://httpbin.org/get with the URL encoded parameter email set to 22f3000819@ds.study.iitm.ac.in What is the JSON output of the command? (Paste only the JSON body, not the headers)",
    "Let's make sure you know how to use npx and prettier. Download README.md. In the directory where you downloaded it, make sure it is called README.md, and run npx -y prettier@3.4.2 README.md | sha256sum. What is the output of the command?",
    "Let's make sure you can write formulas in Google Sheets. Type this formula into Google Sheets. (It won't work in Excel) `=SUM(ARRAY_CONSTRAIN(SEQUENCE(100, 100, 5, 2), 1, 10))` What is the result?",
"Let's make sure you can write formulas in Excel. Type this formula into Excel. Note: This will ONLY work in Office 365. `=SUM(TAKE(SORTBY({13,11,0,9,5,0,15,2,12,15,5,0,2,0,14,9}, {10,9,13,2,11,8,16,14,7,15,5,4,6,1,3,12}), 1, 9))` What is the result? Note: If you get #NAME? you have the wrong version of Excel. Find a friend for whom this works.",
    "Just above this paragraph, there's a hidden input with a secret value. What is the value in the hidden input?",
    "How many Wednesdays are there in the date range 1987-06-21 to 2009-03-20?",
    "Download and unzip file q-extract-csv-zip.zip which has a single extract.csv file inside. What is the value in the \"answer\" column of the CSV file?",
    "Let's make sure you know how to use JSON. Sort this JSON array of objects by the value of the age field. In case of a tie, sort by the name field. Paste the resulting JSON below without any spaces or newlines. `[{"name":"Alice","age":3},{"name":"Bob","age":14},{"name":"Charlie","age":94},{"name":"David","age":67},{"name":"Emma","age":64},{"name":"Frank","age":60},{"name":"Grace","age":70},{"name":"Henry","age":99},{"name":"Ivy","age":2},{"name":"Jack","age":86},{"name":"Karen","age":96},{"name":"Liam","age":22},{"name":"Mary","age":10},{"name":"Nora","age":48},{"name":"Oscar","age":28},{"name":"Paul","age":22}]` Sorted JSON:",
    "Download q-multi-cursor-json.txt  and use multi-cursors and convert it into a single JSON object, where key=value pairs are converted into {key: value, key: value, ...}. What's the result when you paste the JSON at tools-in-data-science.pages.dev/jsonhash and click the Hash button?",
    "Let's make sure you know how to select elements using CSS selectors. Find all <div>s having a foo class in the hidden element below. What's the sum of their data-value attributes? Sum of data-value attributes:",
    "Download and process the files in  which contains three files with different encodings: data1.csv: CSV file encoded in CP-1252 data2.csv: CSV file encoded in UTF-8 data3.txt: Tab-separated file encoded in UTF-16 Each file has 2 columns: symbol and value. Sum up all the values where the symbol matches › OR Œ OR … across all three files. What is the sum of all values associated with these symbols?",
    "Let's make sure you know how to use GitHub. Create a GitHub account if you don't have one. Create a new public repository. Commit a single JSON file called email.json with the value {"email": "22f3000819@ds.study.iitm.ac.in"} and push it. Enter the raw Github URL of email.json so we can verify it. (It might look like https://raw.githubusercontent.com/[GITHUB ID]/[REPO NAME]/main/email.json.)",
    "Download q-replace-across-files.zip and unzip it into a new folder, then replace all "IITM" (in upper, lower, or mixed case) with "IIT Madras" in all files. Leave everything as-is - don't change the line endings. What does running cat * | sha256sum in that folder show in bash?",
    "Download q-list-file-attributes.zip and extract it. Use ls with options to list all files in the folder along with their date and file size. What's the total size of all files at least 1018 bytes large and modified on or after Wed, 10 Dec, 2008, 1:37 am IST? Don't copy from inside the ZIP file or use Windows Explorer to unzip. That destroys the timestamps. Extract using unzip, 7-Zip or similar utilities and check the timestamps.",
    "Download q-move-rename-files.zip and extract it. Use mv to move all files under folders into an empty folder. Then rename all files replacing each digit with the next. 1 becomes 2, 9 becomes 0, a1b9c.txt becomes a2b0c.txt. What does running grep . * | LC_ALL=C sort | sha256sum in bash on that folder show?",
    "Download q-compare-files.zip and extract it. It has 2 nearly identical files, a.txt and b.txt, with the same number of lines. How many lines are different between a.txt and b.txt?",
    "There is a tickets table in a SQLite database that has columns type, units, and price. Each row is a customer bid for a concert ticket.type	units	price BRONZE	408	1.44 Gold	327	1.8 BRONZE	962	1.46 Gold	185	0.77 gold	88	1.5 ... What is the total sales of all the items in the "Gold" ticket type? Write SQL to calculate it. Get all rows where the Type is "Gold". Ignore spaces and treat mis-spellings like GOLD, gold, etc. as "Gold". Calculate the sales as Units * Price, and sum them up.",

]

# Compute embeddings for the questions
question_embeddings = model.encode(questions, convert_to_tensor=True)

def find_best_match(user_input, temp_file_path=None):
    user_embedding = model.encode(user_input, convert_to_tensor=True)
    similarities = util.pytorch_cos_sim(user_embedding, question_embeddings)
    text = user_input
    # Get the most similar question
    best_match_idx = similarities.argmax()
    if best_match_idx == 0:
        return q1()
    elif best_match_idx == 1:
        # Regular expression to match the email
        match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)

        return q2(match.group())
    elif best_match_idx == 2:
        return q3(temp_file_path=temp_file_path)
    elif best_match_idx == 6:
        from datetime import datetime, timedelta

        text = "How many Wednesdays are there in the date range 1987-06-21 to 2009-03-20?"

        # Extract the day and dates using regex
        match = re.search(r'How many (\w+)s? .*? (\d{4}-\d{2}-\d{2}) to (\d{4}-\d{2}-\d{2})\?', text)

        if match:
            day_name = match.group(1)  # "Wednesday"
            start_date = datetime.strptime(match.group(2), "%Y-%m-%d")
            end_date = datetime.strptime(match.group(3), "%Y-%m-%d")
        else:
            return "Invalid input format"

        # Call the function with the extracted values
        return q7(day_name, start_date, end_date)
    return questions[best_match_idx]
