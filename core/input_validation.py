import re

def is_raw_input(text: str) -> tuple[bool, str]:
    """Check if the text contains only raw inputs (hashes, IPs, domains, or URLs)."""
    patterns = {
        'md5': r'^[a-fA-F0-9]{32}$',
        'sha1': r'^[a-fA-F0-9]{40}$',
        'sha256': r'^[a-fA-F0-9]{64}$',
        'ip': r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$',
        'domain': r'^[a-zA-Z0-9][-a-zA-Z0-9.]*\.[a-zA-Z]{2,}$',
        'url': r'^https?://[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b[-a-zA-Z0-9()@:%_\+.~#?&//=]*$'
    }
    
    words = text.strip().split()
    if not words:
        return False, ""
    
    # Check if all words match the same pattern type
    for pattern_type, pattern in patterns.items():
        if all(re.match(pattern, word) for word in words):
            return True, pattern_type.upper()
    
    return False, ""
