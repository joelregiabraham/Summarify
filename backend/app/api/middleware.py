from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.config import get_settings
import time
import asyncio
from collections import defaultdict

class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self.settings = get_settings()
        self.requests = defaultdict(list)

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        now = time.time()
        
        # Clean old requests
        self.requests[client_ip] = [
            req_time for req_time in self.requests[client_ip]
            if now - req_time < self.settings.RATE_LIMIT_PERIOD
        ]
        
        # Check rate limit
        if len(self.requests[client_ip]) >= self.settings.RATE_LIMIT_REQUESTS:
            return JSONResponse(
                status_code=429,
                content={"detail": "Rate limit exceeded"}
            )
        
        self.requests[client_ip].append(now)
        response = await call_next(request)
        return response