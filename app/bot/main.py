import logging

from aiogram import Bot, Dispatcher, Router
from aiogram.types import ErrorEvent
from aiogram_dialog import AccessSettings, DialogManager, StartMode, setup_dialogs
from dishka import make_async_container
from dishka.integrations.aiogram import setup_dishka

from app.bot.dialogs.menu.dialog import menu_dialog
from app.bot.handlers.start import start_router
from app.bot.ioc import DepsProvider
from app.bot.misc import bot, dp
from app.bot.states import Menu
from app.core.config import (
    BotSettings,
    FastAPISettings,
    get_bot_settings,
    get_fastapi_settings,
)

__BOT_SETTINGS: BotSettings = get_bot_settings()
__FASTAPI_SETTINGS: FastAPISettings = get_fastapi_settings()

main_router = Router()


def register_dialogs(router: Router):
    """
    Register all dialogs in the router
    """

    router.include_router(start_router)
    router.include_router(menu_dialog)


@main_router.error()
async def error_handler(event: ErrorEvent, dialog_manager: DialogManager):
    logging.error("Error occurred: %s", event.exception, exc_info=event.exception)

    await dialog_manager.start(
        Menu.main,
        mode=StartMode.RESET_STACK,
        access_settings=AccessSettings(__BOT_SETTINGS.admin_ids),
    )


async def setup_dispatcher(dp: Dispatcher):
    logging.info("Admin IDs: %s", __BOT_SETTINGS.admin_ids)
    container = make_async_container(DepsProvider())
    setup_dishka(container=container, router=dp)
    dp.include_router(main_router)
    register_dialogs(dp)
    setup_dialogs(dp)


async def start_pooling():
    await setup_dispatcher(dp)
    await dp.start_polling(bot, skip_updates=True)


async def setup_webhook(bot: Bot):
    await setup_dispatcher(dp)
    await bot.delete_webhook(drop_pending_updates=__BOT_SETTINGS.drop_pending_updates)
    await bot.set_webhook(
        __FASTAPI_SETTINGS.webhook_url, secret_token=__BOT_SETTINGS.secret_token
    )
