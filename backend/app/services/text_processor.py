from app.models.request import SummarizeRequest
from app.models.response import SummarizeResponse
import time

class TextProcessor:
    def __init__(self, claude_service):
        self.claude_service = claude_service

    async def process_text(self, request: SummarizeRequest) -> SummarizeResponse:
        start_time = time.time()
        
        # Generate summary
        summary = await self.claude_service.generate_summary(request)
        
        # Calculate metrics
        processing_time = time.time() - start_time
        
        return SummarizeResponse(
            summary=summary,
            original_length=len(request.content),
            summary_length=len(summary),
            processing_time=processing_time
        )