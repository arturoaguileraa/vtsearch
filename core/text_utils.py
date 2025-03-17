def translate_to_english(text: str) -> str:
    from core.ai_client import query_gemini
    translation_prompt = f"Translate this text to English, without replying. Only output the translation, nothing else: \n{text}"
    return query_gemini(translation_prompt)