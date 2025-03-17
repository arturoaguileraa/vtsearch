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
        "is_signed": "signed",
        "p2p_cnc": "suspicious-udp",
        "resolves_many_domains": "nxdomain",
        "communicates_with_dga": "suspicious-dns"
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
        "tld": "tld",
        "depth": "depth",
        "a_record": "a_record",
        "a_record_ttl": "a_record_ttl",
        "aaaa_record": "aaaa_record",
        "aaaa_record_ttl": "aaaa_record_ttl",
        "caa_record": "caa_record",
        "cname_record": "cname_record",
        "dname_record": "dname_record",
        "mx_record": "mx_record",
        "ns_record": "ns_record",
        "soa_record": "soa_record",
        "txt_record": "txt_record",
        "category": "category",
        "creation_date": "creation_date",
        "last_update_date": "last_update_date",
        "popularity_rank": "popularity_rank",
        "positive_detections": "p",
        "reputation": "reputation",
        "ssl_issuer": "ssl_issuer",
        "ssl_serial": "ssl_serial",
        "ssl_subject": "ssl_subject",
        "ssl_thumbprint": "ssl_thumbprint",
        "whois_contains": "whois",
        "parent_domain": "parent_domain",
        "threat_actor": "threat_actor"
    },
    "IP": {
        "ip_cidr_range": "ip",
        "autonomous_system_number": "asn",
        "autonomous_system_owner": "aso",
        "country": "country",
        "continent": "continent",
        "comment": "comment",
        "comment_author": "comment_author",
        "positive_detections": "p",
        "antivirus_label": "engines",
        "reputation": "reputation",
        "domain_resolutions_count": "domain_resolutions_count",
        "detected_communicating_files_count": "detected_communicating_files_count",
        "communicating_files_max_detections": "communicating_files_max_detections",
        "detected_downloaded_files_count": "detected_downloaded_files_count",
        "downloaded_files_max_detections": "downloaded_files_max_detections",
        "detected_referring_files_count": "detected_referring_files_count",
        "referring_files_max_detections": "referring_files_max_detections",
        "detected_urls_count": "detected_urls_count",
        "urls_max_detections": "urls_max_detections",
        "ssl_issuer": "ssl_issuer",
        "ssl_serial": "ssl_serial",
        "ssl_subject": "ssl_subject",
        "ssl_thumbprint": "ssl_thumbprint",
        "whois_contains": "whois",
        "last_modification_date": "lm",
        "jarm": "jarm",
        "ssl_not_before": "ssl_not_before",
        "ssl_not_after": "ssl_not_after",
        "threat_actor": "threat_actor",
        "has_detected_downloaded_files": "tag:detected_downloaded_files",
        "has_detected_urls": "tag:detected_urls",
        "has_detected_communicating_files": "tag:detected_communicating_files",
        "has_detected_files_referring": "tag:detected_referring_files"
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
    elif vt_key in ["p", "s", "us"]:  # Fields that use + suffix for minimum values REVISAR
        return f"{value}+"
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
            if isinstance(field_data, bool) and field_data:
                vt_query.append(f"tag:{vt_key}")
            elif isinstance(field_data, dict):
                prefix = "NOT " if field_data.get("is_negative", False) else ""
                values = field_data["value"]
                if isinstance(values, list):
                    for value in values:
                        vt_query.append(f"{prefix}{vt_key}:{format_value(field, vt_key, value)}")
                elif isinstance(values, bool) and values:
                    print("AAG - Warning: Boolean value found in field_data.")
                    vt_query.append(f"tag:{vt_key}")  # Esto en verdad no debería de ocurrir nunca ya que un bool no tiene value.
                else:
                    vt_query.append(f"{prefix}{vt_key}:{format_value(field, vt_key, values)}")
    
    return " ".join(vt_query)
