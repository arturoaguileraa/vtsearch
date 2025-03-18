from typing import Dict, Union

# Field mappings for different query categories
FIELD_MAPPINGS = {
    "FILE": {
        "file_type": "type",
        "min_file_size": "size",
        "max_file_size": "size",
        "positive_detections": "p",
        "antivirus_label": "engines",
        "behavior_report": "behavior",
        "file_metadata": "metadata",
        "file_signature": "signature",
        "downloaded_from": "itw",
        "file_name": "name",
        "tags": "tag",
        "last_seen_after": "ls",
        "last_seen_before": "ls",
        "first_submission_after": "fs",
        "first_submission_before": "fs",
        "last_analysis_after": "la",
        "last_analysis_before": "la",
        "children_positives": "cp",
        "times_submitted": "s",
        "unique_sources": "us",
        "is_signed": "tag:signed",
        "p2p_cnc": "tag:suspicious-udp",
        "resolves_many_domains": "tag:nxdomain",
        "communicates_with_dga": "tag:suspicious-dns"
    },
    "URL": {
        "url_contains": "url",
        "last_serving_ip": "ip",
        "tld": "tld",
        "positive_detections": "p",
        "hostname_contains": "hostname",
        "path_contains": "path",
        "query_value_contains": "query_value",
        "http_header_contains": "header",
        "antivirus_label": "engines",
        "title_contains": "title",
        "categories_contains": "category",
        "tags": "tag",
        "last_seen_after": "ls",
        "last_seen_before": "ls",
        "first_seen_after": "fs",
        "first_seen_before": "fs",
        "last_analysis_after": "la",
        "last_analysis_before": "la",
        "main_icon_dhash": "main_icon_dhash",
        "reputation": "reputation",
        "times_submitted": "s",
        "submitter": "submitter",
        "first_submitter": "first_submitter",
        "cookie": "cookie",
        "cookie_value": "cookie_value",
        "http_header_key": "header",
        "http_header_value": "header_value",
        "password_protected": "have:password",
        "exact_path": "exact_path",
        "extension": "extension",
        "port": "port",
        "query_field": "query_field",
        "query_value": "query_value",
        "redirects_to": "redirects_to",
        "response_code": "response_code",
        "response_positives": "response_positives",
        "response_size": "response_size",
        "scheme": "scheme",
        "tracker": "tracker",
        "parent_domain": "parent_domain",
        "threat_actor": "threat_actor",
        "targeted_brand": "targeted_brand"
    },
    "DOMAIN": {
        "domain_contains": "domain",
        "domain_depth": "depth",
        "tld": "tld",
        "categories_contains": "category",
        "positive_detections": "p",
        "antivirus_label": "engines",
        "popularity_rank": "popularity_rank",
        "whois_contains": "whois",
        "tags": "tag",
        "resolution_ttl": "ttl",
        "txt_record_contains": "txt_record",
        "creation_update_date_after": ["creation_date", "last_update_date"],
        "has_detected_downloaded_files": "detected_downloaded_files_count:1+",
        "has_detected_urls": "detected_urls_count:1+",
        "has_detected_communicating_files": "detected_communicating_files_count:1+",
        "has_detected_files_referring": "detected_referring_files_count:1+"

    },
    "IP": {
        "ip_cidr_range": "ip",
        "positive_detections": "p",
        "antivirus_label": "engines",
        "tags": "tag",
        "whois_contains": "whois",
        "country": "country",
        "autonomous_system_contains": "aso",
        "domain_resolutions_count": "domain_resolutions_count",
        "has_detected_downloaded_files": "detected_downloaded_files_count:1+",
        "has_detected_urls": "detected_urls_count:1+",
        "has_detected_communicating_files": "detected_communicating_files_count:1+",
        "has_detected_files_referring": "detected_referring_files_count:1+"
    }
}

def format_value(field: str, vt_key: str, value: Union[str, int, float, bool]) -> str:
    """Applies custom formatting for size (bytes to KB/MB), dates, range fields, and boolean tags."""
    if vt_key == "size":  # Convert size from bytes to KB or MB
        if isinstance(value, (int, float)):
            if value < 1024:
                formatted_value = f"{int(value)}"  # Keep in bytes
            elif value < 1048576:
                formatted_value = f"{int(value / 1024)}KB"
            else:
                formatted_value = f"{int(value / (1024 * 1024))}MB"
            return f"{formatted_value}+" if "min" in field else f"{formatted_value}-"

    elif vt_key in ["ls", "fs", "la"]:  # Handle timestamps
        return f"{value}+" if "after" in field else f"{value}-"

    elif vt_key in ["p", "s", "us"]:  # Fields that use + suffix for minimum values
        return f"{value}+"

    # Si el valor es un array de strings, aplicar comillas solo a los que tengan espacios
    elif isinstance(value, list):
        return " ".join(f'"{v}"' if " " in v else v for v in value)

    # Si el valor es un string con espacios, ponerlo entre comillas
    elif isinstance(value, str) and " " in value:
        return f'\"{value}\"'

    return str(value)

def convert_query_to_vt_format(query_data: dict, category: str) -> str:
    """Converts structured query JSON into VirusTotal search format based on the category."""
    vt_query = []
    
    if category not in FIELD_MAPPINGS:
        return "Error: Invalid category provided."
    
    field_mappings = FIELD_MAPPINGS[category]
    
    for field, vt_key in field_mappings.items():
        if field in query_data:
            field_data = query_data[field]

            # Si es una lista de valores en FIELD_MAPPINGS (como ["creation_date", "last_update_date"])
            if isinstance(vt_key, list):
                or_conditions = []
                for key in vt_key:
                    formatted_value = format_value(field, key, field_data["value"])
                    or_conditions.append(f"{key}:{formatted_value}+")

                vt_query.append(f"( {' OR '.join(or_conditions)} )")
                continue

            # Manejar booleanos (si field_data es True)
            if isinstance(field_data, bool) and field_data:
                vt_query.append(f"{vt_key}")
                continue

            # Manejar negaciones y listas
            if isinstance(field_data, dict):
                prefix = "NOT " if field_data.get("is_negative", False) else ""
                values = field_data["value"]

                if isinstance(values, list):
                    for value in values:
                        vt_query.append(f"{prefix}{vt_key}:{format_value(field, vt_key, value)}")
                elif isinstance(values, bool) and values:
                    print("AAG - Warning: Boolean value found in field_data.")
                    vt_query.append(f"tag:{vt_key}")  # Esto no debería ocurrir nunca, pero es un fallback
                else:
                    vt_query.append(f"{prefix}{vt_key}:{format_value(field, vt_key, values)}")
    
    return " ".join(vt_query)

