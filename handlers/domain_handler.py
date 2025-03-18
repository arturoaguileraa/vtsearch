from pydantic import BaseModel, Field
from typing import Optional, List, Union


class ModifierField(BaseModel):
    """Handles positive and negative conditions for fields."""
    is_negative: bool = Field(False, description="If True, the condition is a negation (e.g., 'not contains Hello World').")
    value: Union[str, List[Union[str, int, float]]] = Field(..., description="The actual value(s) for the field.")

# Define the data model for domain queries
class DomainSearchQuery(BaseModel):
    domain_contains: Optional[ModifierField] = Field(None, description="Domain contains specific text")
    domain_depth: Optional[ModifierField] = Field(None, description="Number of domain levels, can include ranges")
    tld: Optional[ModifierField] = Field(None, description="Top-Level Domain (TLD)")
    categories_contains: Optional[ModifierField] = Field(None, description="Categories contain specific text")
    positive_detections: Optional[ModifierField] = Field(None, description="Number of positive detections, can include ranges like '8+', '20-'")
    antivirus_label: Optional[ModifierField] = Field(None, description="Antivirus label")
    popularity_rank: Optional[ModifierField] = Field(None, description="Popularity index rank, can include ranges like '8+', '20-'")
    whois_contains: Optional[ModifierField] = Field(None, description="WHOIS data contains specific text")
    tags: Optional[ModifierField] = Field(None, description="Tags associated with the domain")
    resolution_ttl: Optional[ModifierField] = Field(None, description="TTL value for resolution, can include ranges like '8+', '20-'")
    txt_record_contains: Optional[ModifierField] = Field(None, description="TXT record contains specific text")
    creation_update_date_after: Optional[ModifierField] = Field(None, description="Creation/Update date after (YYYY-MM-DDTHH:MM:SS)")
    has_detected_downloaded_files: Optional[bool] = Field(False, description="Indicates if the domain has detected downloaded files (true) or not (false)")
    has_detected_urls: Optional[bool] = Field(False, description="Indicates if the domain has detected URLs (true) or not (false)")
    has_detected_communicating_files: Optional[bool] = Field(False, description="Indicates if the domain has detected communicating files (true) or not (false)")
    has_detected_files_referring: Optional[bool] = Field(False, description="Indicates if the domain has detected referring files (true) or not (false)")