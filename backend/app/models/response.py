from pydantic import BaseModel
from typing import Optional

class SummarizeResponse(BaseModel):
    summary: str
    original_length: int
    summary_length: int
    processing_time: float

class ErrorResponse(BaseModel):
    detail: str
    error_code: Optional[str] = None