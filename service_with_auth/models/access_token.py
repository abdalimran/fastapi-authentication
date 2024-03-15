import secrets
from datetime import datetime, timedelta, timezone

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .user import User


def get_expiration_date(duration_seconds: int = 86400) -> datetime:
    return datetime.now(tz=timezone.utc) + timedelta(seconds=duration_seconds)


def generate_token() -> str:
    return secrets.token_urlsafe(32)


class AccessToken(Base):
    __tablename__ = "access_tokens"

    access_token: Mapped[str] = mapped_column(
        String(1024), primary_key=True, default=generate_token
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    expiration_date: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=get_expiration_date
    )

    user: Mapped[User] = relationship("User", lazy="joined")
