from collections.abc import Awaitable, Callable
from typing import Any

from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject

from app.external_api.waifu_pics_api import WaifuPicsAPIClient


class AnimeArtMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        if not isinstance(event, Message):
            return await handler(event, data)

        category = event.text.split("/")[1]

        try:
            data["photo_url"] = await WaifuPicsAPIClient().random_art(
                type="sfw",
                category=category,
            )
        except Exception:
            data["photo_url"] = None

        return await handler(event, data)
