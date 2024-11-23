from anthropic import Anthropic
from app.config import get_settings
from app.models.request import SummarizeRequest
import asyncio

class ClaudeService:
    def __init__(self):
        self.settings = get_settings()
        self.client = Anthropic(api_key=self.settings.ANTHROPIC_API_KEY)

    async def generate_summary(self, request: SummarizeRequest) -> str:
        prompt = self._construct_prompt(request)
        
        try:
            message = await self.client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=1024,
                messages=[{
                    "role": "user",
                    "content": prompt
                }]
            )
            return message.content
        except Exception as e:
            raise Exception(f"Claude API error: {str(e)}")

    def _construct_prompt(self, request: SummarizeRequest) -> str:
        return f"""
        Please summarize the following text at a {request.summary_length} length, 
        maintaining a {request.complexity_level} complexity level. 
        Focus on key information and main ideas:

        {request.content}
        """