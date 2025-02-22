from fastapi import APIRouter, UploadFile, File
from services.ollama_service import query_ollama
from utils.pdf_parser import extract_text_from_pdf

router = APIRouter()

@router.get("/")
def health_check():
    return {"message": "API está rodando"}

@router.post("/query")
async def query_model(payload: dict):
    response = await query_ollama(payload["prompt"])
    return {"response": response}

@router.post("/extract")
async def extract_from_pdf(file: UploadFile = File(...)):
    text = extract_text_from_pdf(await file.read())
    return {"extracted_text": text}