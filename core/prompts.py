CLASSIFICATION_PROMPT = """
You are an expert computer science assistant. You will be provided with a query asking for type of things and must classify it into one of the following categories: "FILE", "URL", "DOMAIN", or "IP".

Examples:
- "I want malicious PEs" → "FILE"
- "Check the reputation of 8.8.8.8" → "IP"
- "Analyze www.example.com on VirusTotal" → "DOMAIN"
- "Verify if http://malicious.com is in blacklists" → "URL"

Return only one of these options without additional explanations.

Query:
{query}

Expected output:
"""
