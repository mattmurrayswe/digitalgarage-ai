from pydantic import BaseModel


class ListingOut(BaseModel):
    id: int
    message_id: str
    brand: str | None = None
    model: str | None = None
    year: int | None = None
    price_brl: float | None = None
    status: str
    image: bool
    image_ref: str | None = None

    class Config:
        from_attributes = True
