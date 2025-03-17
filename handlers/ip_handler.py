from pydantic import BaseModel, Field
from typing import Optional, List, Union

class ModifierField(BaseModel):
    """Handles positive and negative conditions for fields."""
    is_negative: bool = Field(False, description="If True, the condition is a negation (e.g., 'not PDF').")
    value: Union[str, List[Union[str, int, float]]] = Field(..., description="The actual value(s) for the field.")

# Define the data model for IP queries
class IPSearchQuery(BaseModel):
    ip_cidr_range: Optional[ModifierField] = Field(None, description="IP CIDR range")
    autonomous_system_number: Optional[ModifierField] = Field(None, description="Autonomous system number (ASN)")
    autonomous_system_owner: Optional[ModifierField] = Field(None, description="Autonomous system owner (ASO)")
    country: Optional[ModifierField] = Field(None, description="Country associated with the IP (ISO ALPHA-2 code)")
    continent: Optional[ModifierField] = Field(None, description="Continent associated with the IP (ISO ALPHA-2 code)")
    comment: Optional[ModifierField] = Field(None, description="Search for IPs with specific VirusTotal Community comments")
    comment_author: Optional[ModifierField] = Field(None, description="Search for IPs with comments from a specific user")
    positive_detections: Optional[ModifierField] = Field(None, description="Number of positive detections, can include ranges like '20+', '31-'")
    antivirus_label: Optional[ModifierField] = Field(None, description="Antivirus label")
    reputation: Optional[ModifierField] = Field(None, description="Reputation score, can include ranges like '-20', '-50'")
    domain_resolutions_count: Optional[ModifierField] = Field(None, description="Domain resolution count, can include ranges like '10+', '50-'")
    detected_communicating_files_count: Optional[ModifierField] = Field(None, description="Number of detected communicating files, can include ranges")
    communicating_files_max_detections: Optional[ModifierField] = Field(None, description="Max detections for communicating files")
    detected_downloaded_files_count: Optional[ModifierField] = Field(None, description="Number of detected downloaded files, can include ranges")
    downloaded_files_max_detections: Optional[ModifierField] = Field(None, description="Max detections for downloaded files")
    detected_referring_files_count: Optional[ModifierField] = Field(None, description="Number of detected referring files, can include ranges")
    referring_files_max_detections: Optional[ModifierField] = Field(None, description="Max detections for referring files")
    detected_urls_count: Optional[ModifierField] = Field(None, description="Number of detected URLs, can include ranges")
    urls_max_detections: Optional[ModifierField] = Field(None, description="Max detections for hosted URLs")
    ssl_issuer: Optional[ModifierField] = Field(None, description="SSL certificate issuer")
    ssl_serial: Optional[ModifierField] = Field(None, description="SSL certificate serial number")
    ssl_subject: Optional[ModifierField] = Field(None, description="SSL certificate subject")
    ssl_thumbprint: Optional[ModifierField] = Field(None, description="SSL certificate thumbprint")
    whois_contains: Optional[ModifierField] = Field(None, description="WHOIS data contains specific text")
    last_modification_date: Optional[ModifierField] = Field(None, description="Last modification date, can include ranges")
    jarm: Optional[ModifierField] = Field(None, description="JARM fingerprint")
    ssl_not_before: Optional[ModifierField] = Field(None, description="SSL certificate start validity date")
    ssl_not_after: Optional[ModifierField] = Field(None, description="SSL certificate end validity date")
    threat_actor: Optional[ModifierField] = Field(None, description="Threat actor associated with the IP")
    has_detected_downloaded_files: Optional[bool] = Field(False, description="Indicates if the IP has detected downloaded files")
    has_detected_urls: Optional[bool] = Field(False, description="Indicates if the IP has detected URLs")
    has_detected_communicating_files: Optional[bool] = Field(False, description="Indicates if the IP has detected communicating files")
    has_detected_files_referring: Optional[bool] = Field(False, description="Indicates if the IP has detected referring files")
