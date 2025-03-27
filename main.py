from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional
from core.query_processing import process_query
from core.input_validation import is_raw_input
from core.text_utils import translate_to_english
from core.security_check import is_security_query
from core.ai_client import AIClient

app = FastAPI()

# Agregar CORS para permitir solicitudes desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str
    category: Optional[str] = Field(None, description="Categoría opcional ('FILE', 'URL', 'DOMAIN', 'IP', 'COLLECTION'). Si no se proporciona, se clasificará automáticamente.")

@app.post("/query/")
async def query_api(request: QueryRequest):
    is_raw, input_type = is_raw_input(request.query)
    if is_raw:
        return {"formatted_query": request.query, "vt_format": request.query, "category": input_type}
    
    client = AIClient("Gemini")  # default provider
    translated_query = translate_to_english(client, request.query)
    
    if not is_security_query(client, translated_query):
        return {"formatted_query": "Mmmm... Are you sure you're asking about malware?", "vt_format": "Mmmm... Are you sure you're asking about malware?", "category": "Error"}
    
    return process_query(client, translated_query, request.category)