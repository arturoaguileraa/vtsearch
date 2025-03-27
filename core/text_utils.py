from core.ai_client import AIClient

def translate_to_english(client: AIClient, text: str) -> str:
    translation_prompt = f"Translate this text to English, without replying. Only output the translation, nothing else: \n{text}"
    return client.query_ai(translation_prompt)