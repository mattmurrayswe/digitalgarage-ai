import json
from pathlib import Path
from app.db import SessionLocal, Base, engine
from app.models import Listing

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "car-leads.ndjson"


def main():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    inserted = 0
    skipped = 0
    for line in DATA_FILE.read_text().splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if "_meta" in row:
            continue
        message_id = row.get("messageId")
        if not message_id:
            skipped += 1
            continue
        exists = db.query(Listing).filter(Listing.message_id == message_id).first()
        if exists:
            skipped += 1
            continue
        item = Listing(
            message_id=message_id,
            group_name=row.get("group"),
            group_id=row.get("groupId"),
            seller_whatsapp=row.get("sellerWhatsApp"),
            brand=row.get("brand"),
            model=row.get("model"),
            year=row.get("year"),
            price_brl=row.get("priceBRL"),
            raw_price_text=row.get("rawPriceText"),
            image=bool(row.get("image")),
            image_ref=row.get("imageRef"),
            source=row.get("source"),
            status=row.get("status") or "pending_review",
            captured_at=row.get("capturedAt"),
            published_at=row.get("publishedAt"),
        )
        db.add(item)
        inserted += 1
    db.commit()
    db.close()
    print(f"import_done inserted={inserted} skipped={skipped}")


if __name__ == "__main__":
    main()
