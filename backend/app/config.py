from pydantic import BaseSettings, Field
from typing import Optional


class Settings(BaseSettings):
    """Configuration settings for the movie recommender preprocessing pipeline"""
    
    # Embedding model configuration
    embedding_model_name: str = Field(
        default="Alibaba-NLP/gte-multilingual-base",
        description="Name of the sentence transformer model for embeddings"
    )
    trust_remote_code: bool = Field(
        default=True,
        description="Whether to trust remote code for the embedding model"
    )
    
    # ChromaDB configuration
    db_path: str = Field(
        default="./long_term_memory",
        description="Path for ChromaDB storage"
    )
    collection_name: str = Field(
        default="imdb_data",
        description="Name of the ChromaDB collection"
    )
    batch_size: int = Field(
        default=5461,
        description="Batch size for loading data to ChromaDB"
    )
    
    # Dataset URLs
    imdb_base_url: str = Field(
        default="https://datasets.imdbws.com",
        description="Base URL for IMDb datasets"
    )
    movielens_url: str = Field(
        default="https://files.grouplens.org/datasets/movielens/ml-32m.zip",
        description="URL for MovieLens 32M dataset"
    )
    kaggle_dataset: str = Field(
        default="alanvourch/tmdb-movies-daily-updates",
        description="Kaggle dataset identifier for TMDB data"
    )
    kaggle_filename: str = Field(
        default="TMDB_all_movies.csv",
        description="Filename within the Kaggle dataset"
    )
    
    # Processing configuration
    max_tags_per_movie: int = Field(
        default=10,
        description="Maximum number of tags to keep per movie"
    )
    
    # Performance settings
    memory_limit_gb: Optional[float] = Field(
        default=None,
        description="Memory limit in GB (optional)"
    )
    
    # Data filtering
    required_title_types: list[str] = Field(
        default=["movie", "tvSeries", "tvMovie"],
        description="Title types to include in the final dataset"
    )

    TOTAL_MESSAGES_SUMMARY_TRIGGER: int = 30
    TOTAL_MESSAGES_AFTER_SUMMARY: int = 5

# Global settings instance
settings = Settings() 