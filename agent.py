from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
from typing import Optional
#from app.utils.openai_client import get_openai_response
from application.utils.file_handler import save_upload_file_temporarily
from application.utils.embedsenttrans import create_embedding
from dotenv import load_dotenv

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
        
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
