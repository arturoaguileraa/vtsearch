from pydantic import BaseModel, Field
from typing import Optional, List, Union

class ModifierField(BaseModel):
    """Handles positive and negative conditions for fields."""
    is_negative: bool = Field(False, description="If True, the condition is a negation (e.g., 'not PDF').")
    value: Union[str, List[Union[str, int, float]]] = Field(..., description="The actual value(s) for the field.")

# Define the data model for IP queries
from pydantic import BaseModel, Field
from typing import Optional, List, Union

# Define the data model for IP queries
class IPSearchQuery(BaseModel):
    ip_cidr_range: Optional[ModifierField] = Field(None, description="IP CIDR range")
    positive_detections: Optional[ModifierField] = Field(None, description="Number of positive detections, can include ranges like '3+', '10-'")
    antivirus_label: Optional[ModifierField] = Field(None, description="Antivirus label")
    tags: Optional[ModifierField] = Field(None, description="Tags associated with the IP")
    whois_contains: Optional[ModifierField] = Field(None, description="WHOIS data contains specific text")
    country: Optional[ModifierField] = Field(None, description="Country associated with the IP. ISO ALPHA 2 code required.")
    autonomous_system_contains: Optional[ModifierField] = Field(None, description="Autonomous system organization or identifier. ISO ALPHA 2 code required.")
    domain_resolutions_count: Optional[ModifierField] = Field(None, description="Number of domain resolutions, can include ranges like '1+', '5-'")
    has_detected_downloaded_files: Optional[bool] = Field(False, description="Indicates if the IP has detected downloaded files")
    has_detected_urls: Optional[bool] = Field(False, description="Indicates if the IP has detected URLs")
    has_detected_communicating_files: Optional[bool] = Field(False, description="Indicates if the IP has detected communicating files")
    has_detected_files_referring: Optional[bool] = Field(False, description="Indicates if the IP has detected referring files")
