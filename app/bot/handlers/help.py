import logging

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from app.bot.filters.chat_type import ChatTypeFilter

help_router = Router()


#########################################
##########      /help       #############
#########################################
@help_router.message(
    F.text,
    ChatTypeFilter(
        chat_type=[
            "private",
            "group",
            "supergroup",
        ]
    ),
    Command("help"),
)
async def command_help_handler(message: Message) -> None:
    logging.info(f"Command /help from {message.from_user.id}")

    help_message = (
        "Help:\n"
        "├── Arts\n"
        "│   ├── /waifu\n"
        "│   ├── /neko\n"
        "│   ├── /shinobu\n"
        "│   ├── /megumin\n"
        "│   ├── /bully\n"
        "│   ├── /cuddle\n"
        "│   ├── /cry\n"
        "│   ├── /hug\n"
        "│   ├── /awoo\n"
        "│   ├── /kiss\n"
        "│   ├── /lick\n"
        "│   ├── /pat\n"
        "│   ├── /smug\n"
        "│   ├── /bonk\n"
        "│   ├── /yeet\n"
        "│   ├── /blush\n"
        "│   ├── /smile\n"
        "│   ├── /wave\n"
        "│   ├── /highfive\n"
        "│   ├── /handhold\n"
        "│   ├── /nom\n"
        "│   ├── /bite\n"
        "│   ├── /glomp\n"
        "│   ├── /slap\n"
        "│   ├── /kill\n"
        "│   ├── /kick\n"
        "│   ├── /happy\n"
        "│   ├── /wink\n"
        "│   ├── /poke\n"
        "│   ├── /dance\n"
        "│   └── /cringe\n"
        "└── Ne pridumal\n"
        "    ├── chto-to\n"
        "    └── chto-to"
    )

    await message.answer(help_message)
    await message.delete()
