import logging

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from app.bot.filters.chat_type import ChatTypeFilter
from app.bot.middlewares.anime_art import AnimeArtMiddleware

arts_router = Router()

arts_router.message.middleware(AnimeArtMiddleware())


#########################################
##########      /waifu      #############
#########################################
@arts_router.message(
    F.text,
    ChatTypeFilter(
        chat_type=[
            "private",
            "group",
            "supergroup",
        ]
    ),
    Command("waifu"),
)
async def command_waifu_handler(
    message: Message,
    photo_url: str,
) -> None:
    logging.info(f"Command /waifu from {message.from_user.id}")

    try:
        if photo_url:
            await message.answer_photo(photo=photo_url)
    finally:
        await message.delete()


#########################################
##########      /neko       #############
#########################################
@arts_router.message(
    F.text,
    ChatTypeFilter(
        chat_type=[
            "private",
            "group",
            "supergroup",
        ]
    ),
    Command("neko"),
)
async def command_neko_handler(
    message: Message,
    photo_url: str,
) -> None:
    logging.info(f"Command /neko from {message.from_user.id}")

    try:
        if photo_url:
            await message.answer_photo(photo=photo_url)
    finally:
        await message.delete()


#########################################
##########      /shinobu    #############
#########################################
@arts_router.message(
    F.text,
    ChatTypeFilter(
        chat_type=[
            "private",
            "group",
            "supergroup",
        ]
    ),
    Command("shinobu"),
)
async def command_shinobu_handler(
    message: Message,
    photo_url: str,
) -> None:
    logging.info(f"Command /shinobu from {message.from_user.id}")

    try:
        if photo_url:
            await message.answer_photo(photo=photo_url)
    finally:
        await message.delete()


#########################################
##########      /megumin    #############
#########################################
@arts_router.message(
    F.text,
    ChatTypeFilter(
        chat_type=[
            "private",
            "group",
            "supergroup",
        ]
    ),
    Command("megumin"),
)
async def command_megumin_handler(
    message: Message,
    photo_url: str,
) -> None:
    logging.info(f"Command /megumin from {message.from_user.id}")

    try:
        if photo_url:
            await message.answer_photo(photo=photo_url)
    finally:
        await message.delete()


#########################################
##########      /bully      #############
#########################################
@arts_router.message(
    F.text,
    ChatTypeFilter(
        chat_type=[
            "private",
            "group",
            "supergroup",
        ]
    ),
    Command("bully"),
)
async def command_bully_handler(
    message: Message,
    photo_url: str,
) -> None:
    logging.info(f"Command /bully from {message.from_user.id}")

    try:
        if photo_url:
            await message.answer_photo(photo=photo_url)
    finally:
        await message.delete()


#########################################
##########      /cuddle     #############
#########################################
@arts_router.message(
    F.text,
    ChatTypeFilter(
        chat_type=[
            "private",
            "group",
            "supergroup",
        ]
    ),
    Command("cuddle"),
)
async def command_cuddle_handler(
    message: Message,
    photo_url: str,
) -> None:
    logging.info(f"Command /cuddle from {message.from_user.id}")

    try:
        if photo_url:
            await message.answer_photo(photo=photo_url)
    finally:
        await message.delete()


#########################################
##########      /cry        #############
#########################################
@arts_router.message(
    F.text,
    ChatTypeFilter(
        chat_type=[
            "private",
            "group",
            "supergroup",
        ]
    ),
    Command("cry"),
)
async def command_cry_handler(
    message: Message,
    photo_url: str,
) -> None:
    logging.info(f"Command /cry from {message.from_user.id}")

    try:
        if photo_url:
            await message.answer_photo(photo=photo_url)
    finally:
        await message.delete()


#########################################
##########      /hug        #############
#########################################
@arts_router.message(
    F.text,
    ChatTypeFilter(
        chat_type=[
            "private",
            "group",
            "supergroup",
        ]
    ),
    Command("hug"),
)
async def command_hug_handler(
    message: Message,
    photo_url: str,
) -> None:
    logging.info(f"Command /hug from {message.from_user.id}")

    try:
        if photo_url:
            await message.answer_photo(photo=photo_url)
    finally:
        await message.delete()


#########################################
##########      /awoo       #############
#########################################
@arts_router.message(
    F.text,
    ChatTypeFilter(
        chat_type=[
            "private",
            "group",
            "supergroup",
        ]
    ),
    Command("awoo"),
)
async def command_awoo_handler(
    message: Message,
    photo_url: str,
) -> None:
    logging.info(f"Command /awoo from {message.from_user.id}")

    try:
        if photo_url:
            await message.answer_photo(photo=photo_url)
    finally:
        await message.delete()


#########################################
##########      /kiss       #############
#########################################
@arts_router.message(
    F.text,
    ChatTypeFilter(
        chat_type=[
            "private",
            "group",
            "supergroup",
        ]
    ),
    Command("kiss"),
)
async def command_kiss_handler(
    message: Message,
    photo_url: str,
) -> None:
    logging.info(f"Command /kiss from {message.from_user.id}")

    try:
        if photo_url:
            await message.answer_photo(photo=photo_url)
    finally:
        await message.delete()


#########################################
##########      /lick       #############
#########################################
@arts_router.message(
    F.text,
    ChatTypeFilter(
        chat_type=[
            "private",
            "group",
            "supergroup",
        ]
    ),
    Command("lick"),
)
async def command_lick_handler(
    message: Message,
    photo_url: str,
) -> None:
    logging.info(f"Command /lick from {message.from_user.id}")

    try:
        if photo_url:
            await message.answer_photo(photo=photo_url)
    finally:
        await message.delete()


#########################################
##########      /pat        #############
#########################################
@arts_router.message(
    F.text,
    ChatTypeFilter(
        chat_type=[
            "private",
            "group",
            "supergroup",
        ]
    ),
    Command("pat"),
)
async def command_pat_handler(
    message: Message,
    photo_url: str,
) -> None:
    logging.info(f"Command /pat from {message.from_user.id}")

    try:
        if photo_url:
            await message.answer_photo(photo=photo_url)
    finally:
        await message.delete()


#########################################
##########      /smug       #############
#########################################
@arts_router.message(
    F.text,
    ChatTypeFilter(
        chat_type=[
            "private",
            "group",
            "supergroup",
        ]
    ),
    Command("smug"),
)
async def command_smug_handler(
    message: Message,
    photo_url: str,
) -> None:
    logging.info(f"Command /smug from {message.from_user.id}")

    try:
        if photo_url:
            await message.answer_photo(photo=photo_url)
    finally:
        await message.delete()


#########################################
##########      /bonk       #############
#########################################
@arts_router.message(
    F.text,
    ChatTypeFilter(
        chat_type=[
            "private",
            "group",
            "supergroup",
        ]
    ),
    Command("bonk"),
)
async def command_bonk_handler(
    message: Message,
    photo_url: str,
) -> None:
    logging.info(f"Command /bonk from {message.from_user.id}")

    try:
        if photo_url:
            await message.answer_photo(photo=photo_url)
    finally:
        await message.delete()


#########################################
##########      /yeet       #############
#########################################
@arts_router.message(
    F.text,
    ChatTypeFilter(
        chat_type=[
            "private",
            "group",
            "supergroup",
        ]
    ),
    Command("yeet"),
)
async def command_yeet_handler(
    message: Message,
    photo_url: str,
) -> None:
    logging.info(f"Command /yeet from {message.from_user.id}")

    try:
        if photo_url:
            await message.answer_photo(photo=photo_url)
    finally:
        await message.delete()


#########################################
##########      /blush      #############
#########################################
@arts_router.message(
    F.text,
    ChatTypeFilter(
        chat_type=[
            "private",
            "group",
            "supergroup",
        ]
    ),
    Command("blush"),
)
async def command_blush_handler(
    message: Message,
    photo_url: str,
) -> None:
    logging.info(f"Command /blush from {message.from_user.id}")

    try:
        if photo_url:
            await message.answer_photo(photo=photo_url)
    finally:
        await message.delete()


#########################################
##########      /smile      #############
#########################################
@arts_router.message(
    F.text,
    ChatTypeFilter(
        chat_type=[
            "private",
            "group",
            "supergroup",
        ]
    ),
    Command("smile"),
)
async def command_smile_handler(
    message: Message,
    photo_url: str,
) -> None:
    logging.info(f"Command /smile from {message.from_user.id}")

    try:
        if photo_url:
            await message.answer_photo(photo=photo_url)
    finally:
        await message.delete()


#########################################
##########      /wave       #############
#########################################
@arts_router.message(
    F.text,
    ChatTypeFilter(
        chat_type=[
            "private",
            "group",
            "supergroup",
        ]
    ),
    Command("wave"),
)
async def command_wave_handler(
    message: Message,
    photo_url: str,
) -> None:
    logging.info(f"Command /wave from {message.from_user.id}")

    try:
        if photo_url:
            await message.answer_photo(photo=photo_url)
    finally:
        await message.delete()


#########################################
##########      /highfive   #############
#########################################
@arts_router.message(
    F.text,
    ChatTypeFilter(
        chat_type=[
            "private",
            "group",
            "supergroup",
        ]
    ),
    Command("highfive"),
)
async def command_highfive_handler(
    message: Message,
    photo_url: str,
) -> None:
    logging.info(f"Command /highfive from {message.from_user.id}")

    try:
        if photo_url:
            await message.answer_photo(photo=photo_url)
    finally:
        await message.delete()


#########################################
##########      /handhold   #############
#########################################
@arts_router.message(
    F.text,
    ChatTypeFilter(
        chat_type=[
            "private",
            "group",
            "supergroup",
        ]
    ),
    Command("handhold"),
)
async def command_handhold_handler(
    message: Message,
    photo_url: str,
) -> None:
    logging.info(f"Command /handhold from {message.from_user.id}")

    try:
        if photo_url:
            await message.answer_photo(photo=photo_url)
    finally:
        await message.delete()


#########################################
##########      /nom        #############
#########################################
@arts_router.message(
    F.text,
    ChatTypeFilter(
        chat_type=[
            "private",
            "group",
            "supergroup",
        ]
    ),
    Command("nom"),
)
async def command_nom_handler(
    message: Message,
    photo_url: str,
) -> None:
    logging.info(f"Command /nom from {message.from_user.id}")

    try:
        if photo_url:
            await message.answer_photo(photo=photo_url)
    finally:
        await message.delete()


#########################################
##########      /bite       #############
#########################################
@arts_router.message(
    F.text,
    ChatTypeFilter(
        chat_type=[
            "private",
            "group",
            "supergroup",
        ]
    ),
    Command("bite"),
)
async def command_bite_handler(
    message: Message,
    photo_url: str,
) -> None:
    logging.info(f"Command /bite from {message.from_user.id}")

    try:
        if photo_url:
            await message.answer_photo(photo=photo_url)
    finally:
        await message.delete()


#########################################
##########      /glomp      #############
#########################################
@arts_router.message(
    F.text,
    ChatTypeFilter(
        chat_type=[
            "private",
            "group",
            "supergroup",
        ]
    ),
    Command("glomp"),
)
async def command_glomp_handler(
    message: Message,
    photo_url: str,
) -> None:
    logging.info(f"Command /glomp from {message.from_user.id}")

    try:
        if photo_url:
            await message.answer_photo(photo=photo_url)
    finally:
        await message.delete()


#########################################
##########      /slap       #############
#########################################
@arts_router.message(
    F.text,
    ChatTypeFilter(
        chat_type=[
            "private",
            "group",
            "supergroup",
        ]
    ),
    Command("slap"),
)
async def command_slap_handler(
    message: Message,
    photo_url: str,
) -> None:
    logging.info(f"Command /slap from {message.from_user.id}")

    try:
        if photo_url:
            await message.answer_photo(photo=photo_url)
    finally:
        await message.delete()


#########################################
##########      /kill       #############
#########################################
@arts_router.message(
    F.text,
    ChatTypeFilter(
        chat_type=[
            "private",
            "group",
            "supergroup",
        ]
    ),
    Command("kill"),
)
async def command_kill_handler(
    message: Message,
    photo_url: str,
) -> None:
    logging.info(f"Command /kill from {message.from_user.id}")

    try:
        if photo_url:
            await message.answer_photo(photo=photo_url)
    finally:
        await message.delete()


#########################################
##########      /kick       #############
#########################################
@arts_router.message(
    F.text,
    ChatTypeFilter(
        chat_type=[
            "private",
            "group",
            "supergroup",
        ]
    ),
    Command("kick"),
)
async def command_kick_handler(
    message: Message,
    photo_url: str,
) -> None:
    logging.info(f"Command /kick from {message.from_user.id}")

    try:
        if photo_url:
            await message.answer_photo(photo=photo_url)
    finally:
        await message.delete()


#########################################
##########      /happy      #############
#########################################
@arts_router.message(
    F.text,
    ChatTypeFilter(
        chat_type=[
            "private",
            "group",
            "supergroup",
        ]
    ),
    Command("happy"),
)
async def command_happy_handler(
    message: Message,
    photo_url: str,
) -> None:
    logging.info(f"Command /happy from {message.from_user.id}")

    try:
        if photo_url:
            await message.answer_photo(photo=photo_url)
    finally:
        await message.delete()


#########################################
##########      /wink       #############
#########################################
@arts_router.message(
    F.text,
    ChatTypeFilter(
        chat_type=[
            "private",
            "group",
            "supergroup",
        ]
    ),
    Command("wink"),
)
async def command_wink_handler(
    message: Message,
    photo_url: str,
) -> None:
    logging.info(f"Command /wink from {message.from_user.id}")

    try:
        if photo_url:
            await message.answer_photo(photo=photo_url)
    finally:
        await message.delete()


#########################################
##########      /poke       #############
#########################################
@arts_router.message(
    F.text,
    ChatTypeFilter(
        chat_type=[
            "private",
            "group",
            "supergroup",
        ]
    ),
    Command("poke"),
)
async def command_poke_handler(
    message: Message,
    photo_url: str,
) -> None:
    logging.info(f"Command /poke from {message.from_user.id}")

    try:
        if photo_url:
            await message.answer_photo(photo=photo_url)
    finally:
        await message.delete()


#########################################
##########      /dance      #############
#########################################
@arts_router.message(
    F.text,
    ChatTypeFilter(
        chat_type=[
            "private",
            "group",
            "supergroup",
        ]
    ),
    Command("dance"),
)
async def command_dance_handler(
    message: Message,
    photo_url: str,
) -> None:
    logging.info(f"Command /dance from {message.from_user.id}")

    try:
        if photo_url:
            await message.answer_photo(photo=photo_url)
    finally:
        await message.delete()


#########################################
##########      /cringe     #############
#########################################
@arts_router.message(
    F.text,
    ChatTypeFilter(
        chat_type=[
            "private",
            "group",
            "supergroup",
        ]
    ),
    Command("cringe"),
)
async def command_cringe_handler(
    message: Message,
    photo_url: str,
) -> None:
    logging.info(f"Command /cringe from {message.from_user.id}")

    try:
        if photo_url:
            await message.answer_photo(photo=photo_url)
    finally:
        await message.delete()
