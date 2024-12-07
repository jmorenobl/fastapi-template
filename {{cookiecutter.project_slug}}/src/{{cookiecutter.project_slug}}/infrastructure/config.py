"""
Base configuration settings.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Base configuration settings"""

    # Project info
    PROJECT_NAME: str = "{{cookiecutter.project_slug}}"
    VERSION: str = "0.1.0"

    # API configurations
    API_V1_PREFIX: str = "/api/v1"

    # Security
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        """Configuration for the settings"""

        env_file = ".env"


settings = Settings()
