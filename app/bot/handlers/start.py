import logging

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import AccessSettings, DialogManager, StartMode

from app.bot.filters.chat_type import ChatTypeFilter
from app.bot.states import Menu
from app.core.config import BotSettings, get_bot_settings

__BOT_SETTINGS: BotSettings = get_bot_settings()

start_router = Router()


@start_router.message(ChatTypeFilter(chat_type="private"), CommandStart())
async def command_start_handler(
    message: Message, dialog_manager: DialogManager
) -> None:
    logging.info(f"Command /start from {message.from_user.id}")

    await dialog_manager.start(
        Menu.main,
        mode=StartMode.RESET_STACK,
        access_settings=AccessSettings(__BOT_SETTINGS.admin_ids),
    )
