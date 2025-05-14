"""
Module for handling configuration settings.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class PostgreSettings(BaseSettings):
    """Configuration settings for PostgreSQL database."""

    user: str
    password: str
    host: str
    port: int
    db: str
    echo: bool = False

    model_config = SettingsConfigDict(
        env_prefix="POSTGRES_",
        env_file=".env",
        env_file_encoding="utf-8",
    )
