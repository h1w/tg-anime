from aiogram.filters import BaseFilter
from aiogram.types import Message


class ChatTypeFilter(BaseFilter):
    """
    Filter by chat type.

    Either a single type as a string or a list of strings can be passed to the class constructor.

    Type of the chat, can be either :code:`private`, :code:`group`, :code:`supergroup` or :code:`channel`

    Source: https://docs.aiogram.dev/en/v3.15.0/api/types/chat.html#module-aiogram.types.chat
    """

    def __init__(self, chat_type: str | list):
        self.chat_type = chat_type

    async def __call__(self, message: Message) -> bool:
        if isinstance(self.chat_type, str):
            return message.chat.type == self.chat_type
        else:
            return message.chat.type in self.chat_type
