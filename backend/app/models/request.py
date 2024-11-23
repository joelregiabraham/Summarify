from pydantic import BaseModel, Field, validator
from typing import Optional
from enum import Enum

class SummaryLength(str, Enum):
    SHORT = "short"
    MEDIUM = "medium"
    LONG = "long"

class ComplexityLevel(str, Enum):
    SIMPLE = "simple"
    MODERATE = "moderate"
    DETAILED = "detailed"

class SummarizeRequest(BaseModel):
    content: str = Field(..., min_length=10)
    summary_length: SummaryLength = Field(default=SummaryLength.MEDIUM)
    complexity_level: ComplexityLevel = Field(default=ComplexityLevel.MODERATE)
    
    @validator('content')
    def validate_content_length(cls, v, values):
        if len(v) > 10000:
            raise ValueError('Content too long')
        return v