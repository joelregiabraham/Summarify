from fastapi import APIRouter, Depends, HTTPException
from app.models.request import SummarizeRequest
from app.models.response import SummarizeResponse
from app.services.claude import ClaudeService
from app.services.text_processor import TextProcessor
from app.dependencies import get_text_processor

router = APIRouter()

@router.post("/summarize", response_model=SummarizeResponse)
async def summarize_text(
    request: SummarizeRequest,
    text_processor: TextProcessor = Depends(get_text_processor)
):
    try:
        return await text_processor.process_text(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))