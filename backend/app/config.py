from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """Application settings and configuration."""
    
    # API Keys
    anthropic_api_key: str = ""
    openai_api_key: str = ""
    
    # Application
    secret_key: str = "dev-secret-key-change-in-production"
    environment: str = "development"
    app_name: str = "AI Cover Letter Generator"
    
    # CORS
    allowed_origins: str = "http://localhost:5173,http://localhost:3000"
    
    # Rate Limiting
    rate_limit_per_minute: int = 10
    
    class Config:
        env_file = ".env"
        case_sensitive = False
    
    @property
    def origins_list(self) -> List[str]:
        """Convert comma-separated origins to list."""
        return [origin.strip() for origin in self.allowed_origins.split(",")]


settings = Settings()

