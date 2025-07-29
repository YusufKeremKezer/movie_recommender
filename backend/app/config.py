from pydantic_settings import BaseSettings
from pydantic import SettingsConfigDict

class Settings(BaseSettings):
    """Configuration settings for the movie recommender preprocessing pipeline"""
    
    # App settings
    TOTAL_MESSAGES_SUMMARY_TRIGGER: int = 30
    TOTAL_MESSAGES_AFTER_SUMMARY: int = 5
    
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()

print(settings.model_dump_json(indent=2))