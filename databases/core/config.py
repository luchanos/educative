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
        extra="ignore",
    )


class MySQLSettings(BaseSettings):
    """Configuration settings for MySQL database."""

    root_password: str
    database: str
    user: str
    password: str
    port: int
    echo: bool = False

    model_config = SettingsConfigDict(
        env_prefix="MYSQL_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )
