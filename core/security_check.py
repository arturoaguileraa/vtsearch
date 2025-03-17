from core.ai_client import query_gemini

def is_security_query(text: str) -> bool:
    """Check if the query is related to security analysis."""
    validation_prompt = """You are a computer science query validator. Determine if the query is related to malware, files, domains, IP, or URLs.
    Return ONLY "true" or "false". Do not give any additional explanation.
    
    Examples:
    "PDF files" -> true
    "give me some domains that are malicious" -> true
    "what's the weather today" -> false
    "tell me a joke" -> false
    "IP with suspicious connections" -> true
    "what's the capital of France" -> false
    
    Query to validate:
    {text}
    
    Output (true/false):"""
    
    response = query_gemini(validation_prompt.format(text=text)).strip().lower()
    return "true" in response