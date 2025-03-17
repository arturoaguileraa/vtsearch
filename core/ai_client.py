import google.generativeai as genai
import os
from core.prompts import CLASSIFICATION_PROMPT
from langchain_ollama import OllamaLLM

# Variable para alternar entre Gemini y Ollama
isOllama = True  # Cambia a False para usar Gemini

# Configurar la API Key para Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

VALID_CATEGORIES = {"FILE", "URL", "DOMAIN", "IP", "COLLECTION"}

def query_ai(prompt: str) -> str:
    """Consulta a Gemini o a Ollama dependiendo del valor de isOllama."""
    if isOllama:
        return query_ollama(prompt)
    
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text.strip() if response and response.text else "Error"
    except Exception:
        return "Error"

def query_ollama(prompt: str) -> str:
    try:
        model = OllamaLLM(model="phi4:14b")
        response_text = model.invoke(prompt)
        return response_text.strip()
    except Exception:
        return "Error"

def classify_query(query_text: str) -> str:
    """Clasifica la consulta en File, URL, Domain o IP usando Gemini u Ollama según la configuración."""
    max_attempts = 10
    attempts = 0
    
    while attempts < max_attempts:
        response_text = query_ai(CLASSIFICATION_PROMPT.format(query=query_text))
        category = response_text.strip().upper()
        if any(valid in category for valid in VALID_CATEGORIES):
            return category
        
        attempts += 1
        
    return "Error"
