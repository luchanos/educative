"""
Module for setting up a SQLAlchemy MySQL database connection.
"""

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from core.config import MySQLSettings


db_config = MySQLSettings()
async_db_url = (
    "mysql+aiomysql://" +
    f"{db_config.user}:{db_config.password}" +
    f"@localhost:{db_config.port}" +
    f"/{db_config.database}"
)

async_engine = create_async_engine(
    async_db_url,
    echo=db_config.echo,
)
async_session = async_sessionmaker(
    async_engine,
    expire_on_commit=False,
    class_=AsyncSession,
)
