from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, JSONResponse
import os
from typing import Optional
#from app.utils.openai_client import get_openai_response
from application.utils.file_handler import save_upload_file_temporarily
from application.utils.embedsenttrans import create_embedding
from dotenv import load_dotenv
from typing import List
from pydantic import BaseModel
from application.gas.ga2 import handle_q6, handle_q9
import requests
from application.gas.ga4 import generate_markdown_outline, get_wikipedia_url, extract_headings_from_html

load_dotenv()
RUN_ENV = os.getenv("RUN_ENV", "dev")

if RUN_ENV == "dev":
    print('Create (0) or Load (1) embeddings: ')
    ch = int(input())
    if ch == 0:
        create_embedding()
    else:
        pass
print('Some imports')

from application.questions import find_best_match

print('all imports')

app = FastAPI(title="IITM Assignment API")

print('app created')

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print('cors added')

class NameRequest(BaseModel):
    name: List[str]
@app.post("/api/p2ga2q6", response_class=JSONResponse)
def get_answer(request: NameRequest):
    print(request.name)
    return handle_q6(request.name)

class ClassRequest(BaseModel):
    class_: List[str]
@app.post("/api/p2ga2q9", response_class=JSONResponse)
def get_answer(request: ClassRequest):
    print(request.class_)
    return handle_q9(request.class_)

@app.get("/api/p2ga4q3", response_class=JSONResponse)
async def get_country_outline(country: str):
    """
    API endpoint that returns the markdown outline of the given country Wikipedia page.
    """
    if not country:
        raise HTTPException(status_code=400, detail="Country parameter is required")

    # Fetch Wikipedia page
    url = get_wikipedia_url(country)
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=404, detail=f"Error fetching Wikipedia page: {e}")

    # Extract headings and generate markdown outline
    headings = extract_headings_from_html(response.text)
    if not headings:
        raise HTTPException(status_code=404, detail="No headings found in the Wikipedia page")

    markdown_outline = generate_markdown_outline(headings)
    return {"outline": f"{markdown_outline}"}

@app.post("/api/")
async def process_question(
    question: str = Form(...),
    file: Optional[UploadFile] = File(None)
):
    print('processing question')
    try:
        # Save file temporarily if provided
        temp_file_path = None
        if file:
            temp_file_path = await save_upload_file_temporarily(file)
        
        # Get answer from OpenAI
        answer = find_best_match(question, temp_file_path)
        if type(answer) == str:
            return {"answer": answer}
        else:
            return StreamingResponse(answer, media_type='image/webp', headers={"Content-Disposition": "attachment; filename=output.webp"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
