# Dispatcher
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.base import DefaultKeyBuilder
from aiogram.fsm.storage.redis import RedisStorage

from app.core.config import (
    BotSettings,
    RedisSettings,
    get_bot_settings,
    get_redis_settings,
)

__BOT_SETTINGS: BotSettings = get_bot_settings()
__REDIS_SETTINGS: RedisSettings = get_redis_settings()

key_builder = DefaultKeyBuilder(with_destiny=True)
storage = RedisStorage.from_url(
    __REDIS_SETTINGS.redis_dsn.unicode_string(), key_builder=key_builder
)
dp = Dispatcher(storage=storage)

# Bot
default_bot_properties = DefaultBotProperties(parse_mode=ParseMode.HTML)
bot = Bot(token=__BOT_SETTINGS.token, default=default_bot_properties)
