import google.generativeai as genai
import os
from core.prompts import CLASSIFICATION_PROMPT
from langchain_ollama import OllamaLLM

# Modelos IA según proveedor
AI_MODELS = {
    "Ollama": "phi4:14b", 
    "Gemini": "gemini-1.5-flash"
}

class AIClient():

    def __init__(self, provider: str):
        if provider not in AI_MODELS:
            raise ValueError(f"Proveedor inválido, debe elegir entre {', '.join(AI_MODELS.keys())}.")

        self.provider = provider
        self.model = AI_MODELS[provider]


    def query_ai(self, prompt: str) -> str:
        """Consulta al proveedor de IA con el que se ha configurado."""
        provider_mapping = {
            "Ollama": self._query_ollama,
            "Gemini": self._query_gemini,
        }
        
        try:
            return provider_mapping[self.provider](prompt)
        except KeyError:
            raise ValueError(f"Proveedor desconocido: {self.provider}")
          

    def _query_gemini(self, prompt: str) -> str:
        # Configurar la API Key para Gemini
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        try:
            model = genai.GenerativeModel(model_name=self.model)
            response = model.generate_content(prompt)
        except Exception as e:
            return f"Error: {str(e)}"
        
        return response.text.strip() if response and response.text else "Sin respuesta."


    def _query_ollama(self, prompt: str) -> str:
        try:
            model = OllamaLLM(model=self.model)
            response_text = model.invoke(prompt)
        except Exception as e:
            return f"Error: {str(e)}"
        
        return response_text.strip()
    

    def classify_query(self, query_text: str) -> str:
        """Clasifica la consulta en File, URL, Domain o IP usando el proveedor configurado."""
        VALID_CATEGORIES = {"FILE", "URL", "DOMAIN", "IP", "COLLECTION"}
        max_attempts = 10
        attempts = 0
        
        while attempts < max_attempts:
            response_text = self.query_ai(CLASSIFICATION_PROMPT.format(query=query_text))
            category = response_text.strip().upper()
            if any(valid in category for valid in VALID_CATEGORIES):
                return category
            
            attempts += 1
            
        return "Error en la clasificación."
