import logging
from typing import Annotated

from aiogram.types import Update
from fastapi import APIRouter, Header

from app.bot.misc import bot, dp
from app.core.config import (
    BotSettings,
    FastAPISettings,
    get_bot_settings,
    get_fastapi_settings,
)

__FASTAPI_SETTINGS: FastAPISettings = get_fastapi_settings()
__BOT_SETTINGS: BotSettings = get_bot_settings()

webhook_router = APIRouter()


@webhook_router.post(__FASTAPI_SETTINGS.webhook_path)
async def webhook(
    update: dict,
    x_telegram_bot_api_secret_token: Annotated[str | None, Header()] = None,
) -> None | dict:
    if x_telegram_bot_api_secret_token != __BOT_SETTINGS.secret_token:
        logging.error("Wrong secret token!")
        return {"status": "error", "message": "Wrong secret token !"}
    telegram_update = Update(**update)
    logging.debug("Webhook update: %s", telegram_update)
    await dp.feed_webhook_update(bot=bot, update=telegram_update)
    return {"ok": True}
