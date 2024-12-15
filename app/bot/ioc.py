from collections.abc import AsyncGenerator
from typing import Self

from dishka import Provider, Scope, provide

from app.bot.common.uow import UoW
from app.bot.database.db import SessionFactory


class DepsProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def get_uow(self: Self) -> AsyncGenerator[UoW, None]:
        async with SessionFactory() as session:
            yield UoW(session)
