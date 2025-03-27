from core.ai_client import AIClient

def test_gemini_query():
    """Prueba la función query_gemini para verificar la conexión con Gemini y la respuesta."""
    test_prompt = "Translate 'Hello world' to Spanish in JSON format: {\"translation\": \"Hola mundo\"}"

    try:
        print("🔄 Enviando consulta a Gemini...")
        client = AIClient("Gemini")
        response = client.query_ai(test_prompt)

        if response:
            print("✅ Conexión exitosa con Gemini!")
            print("🔹 Respuesta de Gemini:", response)
        else:
            print("⚠️ La API respondió pero no devolvió un texto válido.")

    except Exception as e:
        print(f"❌ Error conectando con Gemini: {str(e)}")

# Ejecutar prueba
if __name__ == "__main__":
    test_gemini_query()
