import logging
from core.logical_conversion import convert_to_logical_expression
from handlers.modifier_handler import process_logical_query
from core.ai_client import classify_query

# Configurar logging para mostrar información detallada
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def test_pipeline(query: str):
    """Prueba el flujo de conversión de una consulta en lenguaje natural a una consulta de VirusTotal Intelligence."""

    logging.info(f"🔍 Consulta original: {query}")

    # Paso 1: Convertir a expresión lógica
    logical_query = convert_to_logical_expression(query)
    logging.info(f"📌 Expresión lógica generada: {logical_query}")

    # Paso 2: Clasificar la categoría automáticamente
    category = classify_query(query)
    logging.info(f"📂 Categoría detectada: {category}")

    # Paso 3: Procesar los términos y convertirlos en operadores de VT Intelligence
    transformed_query = process_logical_query(logical_query, category)
    logging.info(f"✅ Consulta final convertida: {transformed_query}")

    return transformed_query

if __name__ == "__main__":
    # Prueba con diferentes consultas SIN especificar la categoría
    test_queries = [
        "malware y tipo pdf",
    ]

    for query in test_queries:
        print("\n=============================")
        print(f"🔎 Probando consulta: {query}")
        print("=============================")
        final_query = test_pipeline(query)
        print(f"🎯 Resultado Final: {final_query}")
