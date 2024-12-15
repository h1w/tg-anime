from bot.models.base import Base
from bot.models.fields import chat_id_bigint, uuid_pk
from sqlalchemy.orm import Mapped


class Channel(Base):
    __tablename__ = "channels"
    id: Mapped[uuid_pk]
    name: Mapped[str]
    chat_id: Mapped[chat_id_bigint]
