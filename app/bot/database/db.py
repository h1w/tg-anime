from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.core.config import DbSettings, get_db_settings

__DB_SETTINGS: DbSettings = get_db_settings()

engine = create_async_engine(
    __DB_SETTINGS.postgres_dsn.unicode_string(),
    echo=__DB_SETTINGS.debug,
)

SessionFactory = async_sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)
