from pydantic import BaseModel, Field
from typing import Optional, List, Union

class ModifierField(BaseModel):
    """Handles positive and negative conditions for fields."""
    is_negative: bool = Field(False, description="If True, the condition is a negation (e.g., 'not contains Hello World').")
    value: Union[str, List[Union[str, int, float]]] = Field(..., description="The actual value(s) for the field.")

# Define the data model for URL queries
class URLSearchQuery(BaseModel):
    url_contains: Optional[ModifierField] = Field(None, description="The specific text that is contained in the URL")
    last_serving_ip: Optional[ModifierField] = Field(None, description="Last serving IP address")
    tld: Optional[ModifierField] = Field(None, description="Top-Level Domain (TLD)")
    positive_detections: Optional[ModifierField] = Field(None, description="Number of positive detections")
    hostname_contains: Optional[ModifierField] = Field(None, description="Hostname contains specific text")
    path_contains: Optional[ModifierField] = Field(None, description="Path contains specific text")
    query_value_contains: Optional[ModifierField] = Field(None, description="Query value contains specific text")
    http_header_contains: Optional[ModifierField] = Field(None, description="HTTP header value contains specific text")
    antivirus_label: Optional[ModifierField] = Field(None, description="Antivirus label")
    title_contains: Optional[ModifierField] = Field(None, description="Title contains specific text")
    categories_contains: Optional[ModifierField] = Field(None, description="Categories contain specific text")
    tags: Optional[ModifierField] = Field(None, description="Tags associated with the URL")
    last_seen_after: Optional[ModifierField] = Field(None, description="Last seen after (YYYY-MM-DDTHH:MM:SS)")
    last_seen_before: Optional[ModifierField] = Field(None, description="Last seen before (YYYY-MM-DDTHH:MM:SS)")
    first_seen_after: Optional[ModifierField] = Field(None, description="First seen after (YYYY-MM-DDTHH:MM:SS)")
    first_seen_before: Optional[ModifierField] = Field(None, description="First seen before (YYYY-MM-DDTHH:MM:SS)")
    last_analysis_after: Optional[ModifierField] = Field(None, description="Last analysis after (YYYY-MM-DDTHH:MM:SS)")
    last_analysis_before: Optional[ModifierField] = Field(None, description="Last analysis before (YYYY-MM-DDTHH:MM:SS)")
    main_icon_dhash: Optional[ModifierField] = Field(None, description="Favicon hash for visual similarity analysis")
    reputation: Optional[ModifierField] = Field(None, description="Reputation score, can include ranges like '70+', '-10'")
    times_submitted: Optional[ModifierField] = Field(None, description="Times submitted, can include ranges like '3', '4+', '10-'")
    submitter: Optional[ModifierField] = Field(None, description="Submitter source (API, web) or country (ISO Alpha-2 code)")
    first_submitter: Optional[ModifierField] = Field(None, description="Country of first submitter (ISO Alpha-2 code)")
    cookie: Optional[ModifierField] = Field(None, description="Cookie value in HTTP response")
    cookie_value: Optional[ModifierField] = Field(None, description="Specific cookie key-value pair")
    http_header_key: Optional[ModifierField] = Field(None, description="HTTP response header key")
    http_header_value: Optional[ModifierField] = Field(None, description="HTTP response header value")
    password_protected: Optional[bool] = Field(False, description="Indicates if the URL is password protected")
    exact_path: Optional[ModifierField] = Field(None, description="Exact URL path")
    extension: Optional[ModifierField] = Field(None, description="File extension associated with the URL")
    port: Optional[int] = Field(None, description="Port number of the HTTP server")
    redirects_to: Optional[ModifierField] = Field(None, description="URL the page redirects to")
    response_code: Optional[ModifierField] = Field(None, description="HTTP response code")
    response_positives: Optional[ModifierField] = Field(None, description="Number of antivirus detections on response content")
    response_size: Optional[ModifierField] = Field(None, description="Size of the content returned, in bytes")
    tracker: Optional[ModifierField] = Field(None, description="Analytics tracker used in the URL")
    parent_domain: Optional[ModifierField] = Field(None, description="Parent domain of the URL")
    threat_actor: Optional[ModifierField] = Field(None, description="Threat actor associated with the URL")
    
    
'''    
    downloads_windows_executable: Optional[bool] = Field(False, description="Indicates if the URL downloads a Windows executable")
    downloads_document: Optional[bool] = Field(False, description="Indicates if the URL downloads a document")
    is_open_directory: Optional[bool] = Field(False, description="Indicates if the URL is an open directory")
    open_directory_lists_executables: Optional[bool] = Field(False, description="Indicates if the open directory lists executables")
    http_response_status: Optional[ModifierField] = Field(None, description="HTTP response status code")
    category: Optional[ModifierField] = Field(None, description="Content category of the domain")
    title: Optional[ModifierField] = Field(None, description="Title contained in the HTML response")
    targeted_brand: Optional[ModifierField] = Field(None, description="Brand targeted by phishing engines")
    scheme: Optional[ModifierField] = Field(None, description="Protocol scheme (HTTP/HTTPS)")
    query_field: Optional[ModifierField] = Field(None, description="Specific query field key")
    query_value: Optional[ModifierField] = Field(None, description="Specific query field value")
'''
