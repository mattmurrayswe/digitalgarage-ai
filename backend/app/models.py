from sqlalchemy import String, Integer, Float, Boolean, Text, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from .db import Base


class Listing(Base):
    __tablename__ = "listings"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    message_id: Mapped[str] = mapped_column(String(128), unique=True, index=True)
    group_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    group_id: Mapped[str | None] = mapped_column(String(128), nullable=True)
    seller_whatsapp: Mapped[str | None] = mapped_column(String(32), nullable=True)
    brand: Mapped[str | None] = mapped_column(String(80), nullable=True)
    model: Mapped[str | None] = mapped_column(String(255), nullable=True)
    year: Mapped[int | None] = mapped_column(Integer, nullable=True)
    price_brl: Mapped[float | None] = mapped_column(Float, nullable=True)
    raw_price_text: Mapped[str | None] = mapped_column(String(120), nullable=True)
    image: Mapped[bool] = mapped_column(Boolean, default=False)
    image_ref: Mapped[str | None] = mapped_column(Text, nullable=True)
    source: Mapped[str | None] = mapped_column(String(64), nullable=True)
    status: Mapped[str] = mapped_column(String(32), default="pending_review", index=True)
    captured_at: Mapped[str | None] = mapped_column(String(64), nullable=True)
    published_at: Mapped[str | None] = mapped_column(String(64), nullable=True)
    created_at: Mapped[str] = mapped_column(DateTime(timezone=True), server_default=func.now())
