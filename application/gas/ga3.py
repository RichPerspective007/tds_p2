import requests
import os
import re
from dotenv import load_dotenv
import base64
load_dotenv()

def q3_1(question: str = None, file_path: str = None):
    s = re.search(r'meaningless text:(.+)Write', question, re.DOTALL)
    mngl = s.group(1).strip(' \n`<>')
    return f"""import httpx

# API endpoint
API_URL = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"

# Dummy API key
HEADERS = {{
    "Authorization": "Bearer dummy_api_key",
    "Content-Type": "application/json"
}}

# Request payload
DATA = {{
    "model": "gpt-4o-mini",
    "messages": [
        {{"role": "system", "content": "Analyze the sentiment of the following text as GOOD, BAD, or NEUTRAL."}},
        {{"role": "user", "content": "{mngl}"}}
    ]
}}

# Send POST request
try:
    response = httpx.post(API_URL, json=DATA, headers=HEADERS)
    response.raise_for_status()

    # Parse response
    result = response.json()
    print(result)
except httpx.HTTPStatusError as e:
    print(f"HTTP error occurred: {{e.response.status_code}} - {{e.response.text}}")
except Exception as e:
    print(f"An error occurred: {{e}}")"""

def q3_2(question: str = None, file_path: str = None):
    s = re.search(r'(List only [\w\d\s,:]+)', question)
    s.group(1).strip()
    url = "http://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('AIPROXY_TOKEN')}"
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": s.group(1).strip()}]
    }

    response = requests.post(url, json=data, headers=headers)
    response_json = response.json()
    inp_tokens = response_json['usage']['prompt_tokens']

    return f"{inp_tokens}"

def q3_3(question: str = None, file_path: str = None):
    s = re.search(r'required fields:([\w\s\(\)]+).', question)
    dt = s.group(1).strip().split(' ')
    return f"""{{
  "model": "gpt-4o-mini",
  "messages": [
    {{
      "role": "system",
      "content": "Respond in JSON"
    }},
    {{
      "role": "user",
      "content": "Generate 10 random addresses in the US"
    }}
  ],
  "response_format": {{
    "type": "json_schema",
    "json_schema": {{
      "name": "address_response",
      "strict": true,
      "schema": {{
        "type": "object",
        "properties": {{
          "addresses": {{
            "type": "array",
            "items": {{
              "type": "object",
              "properties": {{
                "{dt[0]}": {{
                  "type": "{dt[1].strip('()')}"
                }},
                "{dt[2]}": {{
                  "type": "{dt[3].strip('()')}"
                }},
                "{dt[4]}": {{
                  "type": "{dt[5].strip('()')}"
                }}
              }},
              "required": ["{dt[0]}", "{dt[2]}", "{dt[4]}"],
              "additionalProperties": false
            }}
          }}
        }},
        "required": ["addresses"],
        "additionalProperties": false
      }}
    }}
  }}
}}"""

def q3_4(question: str = None, file_path: str = None):
    with open(file_path, 'rb') as f:
        b64 = base64.b64encode(f.read()).decode('utf-8')  # No newlines
    return f"""{{
  "model": "gpt-4o-mini",
  "messages": [
    {{
      "role": "user",
      "content": [
        {{
          "type": "text",
          "text": "Extract text from this image"
        }},
        {{
          "type": "image_url",
          "image_url": {{
            "url": "data:image/png;base64,{b64}"
          }}
        }}
      ]
    }}
  ]
}}"""

def q3_5(question: str = None, file_path: str = None):
    try:
        s = re.search(r'(Dear[\w\d\s,@.]+\.in)', question)
    except Exception as e:
        return f"Error: {e} in regex"
    try:
        q = s.group(1).splitlines()
        print(len(q), q, sep='\n')
    except Exception as e:
        return f"Error: {e} in splitlines"
    try:
        return f"""{{
  "model": "text-embedding-3-small",
  "input": [
    "{q[0]}",
    "{q[1]}"
  ]
}}"""
    except Exception as e:
        return f"Error: {e} in output"

def q3_6(question: str = None, file_path: str = None):
    return """import numpy as np

def most_similar(embeddings):
    max_similarity = -1
    most_similar_pair = None

    phrases = list(embeddings.keys())

    for i in range(len(phrases)):
        for j in range(i + 1, len(phrases)):
            v1 = np.array(embeddings[phrases[i]])
            v2 = np.array(embeddings[phrases[j]])

            similarity = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

            if similarity > max_similarity:
                max_similarity = similarity
                most_similar_pair = (phrases[i], phrases[j])

    return most_similar_pair"""

def q3_7(question: str = None, file_path: str = None):
    return "http://127.0.0.1:8000/similarity"

def q3_8(question: str = None, file_path: str = None):
    return "http://127.0.0.1:8000/execute"