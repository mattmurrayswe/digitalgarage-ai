from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session

from .db import Base, engine, SessionLocal
from .models import Listing

app = FastAPI(title="digitalgarage-ai API")


@app.on_event("startup")
def startup() -> None:
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/health')
def health():
    return {'status': 'ok'}


@app.get('/listings')
def list_listings(
    status: str | None = Query(default=None),
    limit: int = Query(default=50, ge=1, le=500),
    db: Session = Depends(get_db),
):
    q = db.query(Listing).order_by(Listing.id.desc())
    if status:
        q = q.filter(Listing.status == status)
    rows = q.limit(limit).all()
    return [
        {
            "id": r.id,
            "message_id": r.message_id,
            "brand": r.brand,
            "model": r.model,
            "year": r.year,
            "price_brl": r.price_brl,
            "status": r.status,
            "image": r.image,
            "image_ref": r.image_ref,
        }
        for r in rows
    ]
