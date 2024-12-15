from functools import lru_cache

from pydantic import PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings


class FastAPISettings(BaseSettings):
    debug: bool = False

    api_name: str = ""
    api_desc: str = ""
    api_v1_str: str = ""
    api_host: str = ""
    api_port: int | None = None
    origins: list[str] = []

    class Config:
        env_file_encoding = "utf-8"

    @property
    def webhook_path(self) -> str:
        return f"{self.api_v1_str}/webhook"

    @property
    def webhook_url(self) -> str:
        return f"{self.api_host}{self.webhook_path}"


@lru_cache
def get_fastapi_settings() -> FastAPISettings:
    return FastAPISettings()


class BotSettings(BaseSettings):
    debug: bool = False

    token: str = ""
    admin_ids: list[int] = []
    use_webhook: bool = False
    secret_token: str | None = None
    drop_pending_updates: bool = False

    class Config:
        env_file_encoding = "utf-8"


@lru_cache
def get_bot_settings() -> BotSettings:
    return BotSettings()


class DbSettings(BaseSettings):
    debug: bool = False

    db_name: str = ""
    db_host: str = ""
    db_port: int = 0

    db_user: str = ""
    db_pass: str = ""

    postgres_dsn: PostgresDsn | None = None

    class Config:
        env_file_encoding = "utf-8"


@lru_cache
def get_db_settings() -> DbSettings:
    return DbSettings()


class RedisSettings(BaseSettings):
    redis_dsn: RedisDsn | None = None

    class Config:
        env_file_encoding = "utf-8"


@lru_cache
def get_redis_settings() -> RedisSettings:
    return RedisSettings()
