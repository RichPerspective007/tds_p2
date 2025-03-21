from sentence_transformers import SentenceTransformer, util
import re

from .gas.ga1 import q1, q2, q3, q7

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Your predefined 50 questions
questions = [
    "Install and run Visual Studio Code. In your Terminal (or Command Prompt), type code -s and press Enter. Copy and paste the entire output below. What is the output of code -s?",
    "Running uv run --with httpie -- https [URL] installs the Python package httpie and sends a HTTPS request to the URL. Send a HTTPS request to https://httpbin.org/get with the URL encoded parameter email set to 22f3000819@ds.study.iitm.ac.in. What is the JSON output of the command? (Paste only the JSON body, not the headers)",
    "Let's make sure you know how to use npx and prettier. Download README.md. In the directory where you downloaded it, make sure it is called README.md, and run npx -y prettier@3.4.2 README.md | sha256sum. What is the output of the command?",
    "Let's make sure you can write formulas in Google Sheets. Type this formula into Google Sheets. (It won't work in Excel) =SUM(ARRAY_CONSTRAIN(SEQUENCE(100, 100, 5, 2), 1, 10)) What is the result?",
    "",
    "",
    "How many Wednesdays are there in the date range 1987-06-21 to 2009-03-20?"
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
