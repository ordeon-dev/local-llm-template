from fastapi import APIRouter, UploadFile, File, HTTPException
from services.ollama_service import query_ollama
from utils.pdf_parser import extract_text_from_pdf
from models.request_model import QueryModel
from fastapi.responses import StreamingResponse

router = APIRouter()

@router.get("/")
def health_check():
    return {"message": "API está rodando"}

@router.post("/query")
async def query_model(payload: QueryModel):
    try:
        response = await query_ollama(
            f"""Extraia APENAS o valor total do seguinte texto. Responda SOMENTE o valor total. Texto: {payload.prompt} Resposta:
            """
        )
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/extract")
async def extract_from_pdf(file: UploadFile = File(...)):
    text = extract_text_from_pdf(await file.read())
    return {"extracted_text": text}