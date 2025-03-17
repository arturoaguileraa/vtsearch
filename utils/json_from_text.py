import json
import re

def extract_json_from_text(text: str) -> dict:
    """
    Extracts the first valid JSON object from a given text string.
    
    :param text: The input string containing a JSON structure.
    :return: A dictionary containing the parsed JSON or an error message.
    """
    try:
        # Regular expression to find a JSON object
        json_match = re.search(r"\{.*\}", text, re.DOTALL)
        if json_match:
            json_str = json_match.group()
            return json.loads(json_str)  # Convert string to JSON (dict)
        else:
            return {"error": "No JSON found in text."}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format."}

