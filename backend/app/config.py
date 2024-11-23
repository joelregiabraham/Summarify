from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME: str = "Text Summarizer API"
    DEBUG: bool = False
    ANTHROPIC_API_KEY: str
    MAX_INPUT_LENGTH: int = 10000
    RATE_LIMIT_REQUESTS: int = 100
    RATE_LIMIT_PERIOD: int = 3600  # 1 hour
    
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()