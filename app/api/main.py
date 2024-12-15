import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from starlette.middleware.cors import CORSMiddleware

from app.api.webhook_router import webhook_router
from app.bot.misc import bot
from app.core.config import (
    FastAPISettings,
    get_fastapi_settings,
)

__FASTAPI_SETTINGS: FastAPISettings = get_fastapi_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):  # noqa: ARG001
    """
    Provides a context manager for managing the lifespan of a FastAPI application.

    Inside the `lifespan` context manager, the `before start` and `before stop`
    comments indicate where the startup and shutdown operations should be
    implemented.
    """

    # before start
    logging.info("🚀 Starting application")
    from app.bot.main import setup_webhook

    await setup_webhook(bot)
    yield
    # before stop
    await bot.delete_webhook()
    logging.info("⛔ Stopping application, deleting webhook")


def create_app() -> FastAPI:
    app: FastAPI = FastAPI(
        title=__FASTAPI_SETTINGS.api_name,
        description=__FASTAPI_SETTINGS.api_desc,
        docs_url="/api/docs",
        debug=__FASTAPI_SETTINGS.debug,
        default_response_class=ORJSONResponse,
        lifespan=lifespan,
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=__FASTAPI_SETTINGS.origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(webhook_router)

    return app
