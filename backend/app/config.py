from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Configuration settings for the movie recommender preprocessing pipeline"""
    
    # App settings
    TOTAL_MESSAGES_SUMMARY_TRIGGER: int = 30
    TOTAL_MESSAGES_AFTER_SUMMARY: int = 5
    
    class Config:
        env_file = ".env"  # Specify the location of the environment file
        env_file_encoding = "utf-8"  # Encoding for the environment file


settings = Settings()

