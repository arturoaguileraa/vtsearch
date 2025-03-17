from pydantic import BaseModel, Field
from typing import Optional, List, Union, Literal

class ModifierField(BaseModel):
    """Handles positive and negative conditions for fields."""
    is_negative: bool = Field(False, description="If True, the condition is a negation (e.g., 'not PDF').")
    value: Union[str, List[Union[str, int, float]]] = Field(..., description="The actual value(s) for the field.")

class FileTypeModifierField(ModifierField):
    """Restricts file_type to a fixed set of values."""
    value: Literal["executable", "document", "internet", "image", "audio", "video", "compressed", "apple", "mp3", "pdf", "docx", "svg", "html", "pcap"]

class FileSearchQuery(BaseModel):
    file_type: Optional[FileTypeModifierField] = Field(None, description="File type (supports negation)")
    min_file_size: Optional[ModifierField] = Field(None, description="Minimum file size in bytes (supports negation)")
    max_file_size: Optional[ModifierField] = Field(None, description="Maximum file size in bytes (supports negation)")
    positive_detections: Optional[ModifierField] = Field(None, description="Number of positive detections")
    antivirus_label: Optional[ModifierField] = Field(None, description="Antivirus label (supports negation)")
    behavior_report: Optional[ModifierField] = Field(None, description="Behavior report content (supports negation)")
    file_metadata: Optional[ModifierField] = Field(None, description="File metadata (supports negation)")
    file_signature: Optional[ModifierField] = Field(None, description="File signature (supports negation)")
    downloaded_from: Optional[ModifierField] = Field(None, description="Download source (supports negation)")
    file_name: Optional[ModifierField] = Field(None, description="File name (supports negation)")
    tags: Optional[ModifierField] = Field(None, description="Tags (supports negation)") # TO-DO : Add list of tags
    last_seen_after: Optional[ModifierField] = Field(None, description="Last seen after date (YYYY-MM-DDTHH:MM:SS format) (supports negation)")
    last_seen_before: Optional[ModifierField] = Field(None, description="Last seen before date (YYYY-MM-DDTHH:MM:SS format)  (supports negation)")
    first_submission_after: Optional[ModifierField] = Field(None, description="First submission datetime after (supports negation)")
    first_submission_before: Optional[ModifierField] = Field(None, description="First submission datetime before (supports negation)")
    last_analysis_after: Optional[ModifierField] = Field(None, description="Last analysis datetime after (supports negation)")
    last_analysis_before: Optional[ModifierField] = Field(None, description="Last analysis datetime before (supports negation)")
    children_positives: Optional[ModifierField] = Field(None, description="Maximum number of detections of children files (supports negation)")
    times_submitted: Optional[ModifierField] = Field(None, description="Times submitted (supports negation)")
    unique_sources: Optional[ModifierField] = Field(None, description="Number of unique sources (supports negation)")
    is_signed: Optional[bool] = Field(None, description="Indicates if the file is signed (true) or not (false)")
    p2p_cnc: Optional[bool] = Field(False, description="Indicates if the file exhibits P2P CnC communication (true) or not (false)")
    resolves_many_domains: Optional[bool] = Field(False, description="Indicates if the file resolves many domains resulting in NXDOMAIN replies (true) or not (false)")
    communicates_with_dga: Optional[bool] = Field(False, description="Indicates if the file communicates with DGA CnC domains (true) or not (false)")
