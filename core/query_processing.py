from core.ai_client import classify_query, query_ai
from fastapi import HTTPException
from handlers.file_handler import FileSearchQuery
from handlers.ip_handler import IPSearchQuery
from handlers.url_handler import URLSearchQuery
from handlers.domain_handler import DomainSearchQuery
from utils.json_to_vt import convert_query_to_vt_format
from utils.json_from_text import extract_json_from_text

# Generalized function to process any category
def process_generic_query(user_input: str, schema_model):
    prompt = f"""
    Extract structured data from the following natural language query, without explaining ANYTHING. DO NOT EXPLAIN ANYTHING.
    Use the following schema to construct the JSON where some field has:
    - `is_negative`: to indicate negations.
    
    Schema:
    {schema_model.schema()}
    
    Query: {user_input}
    """
    
    print("Sending prompt to AI model...")
    response = query_ai(prompt)
    print(response)
    
    try:
        structured_data = extract_json_from_text(response)
        
        if not isinstance(structured_data, dict):
            return {"error": "Unexpected response format from AI model."}
        
        return structured_data
    except json.JSONDecodeError:
        return {"error": "Could not interpret the response."}

def process_query(query: str, category: str = None):
    category = category or classify_query(query)
    
    print("Category:", category)
    
    category_mappings = {
        "FILE": (process_generic_query, FileSearchQuery),
        "URL": (process_generic_query, URLSearchQuery),
        "DOMAIN": (process_generic_query, DomainSearchQuery),
        "IP": (process_generic_query, IPSearchQuery)
    }
    
    if category in category_mappings:
        handler_function, schema_model = category_mappings[category]
        formatted_query = handler_function(query, schema_model)
        return {
            "formatted_query": formatted_query,
            "vt_format": convert_query_to_vt_format(formatted_query, category),
            "category": category
        }
    else:
        raise HTTPException(status_code=400, detail="Invalid query category: " + category)
