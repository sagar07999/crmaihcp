from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.models import Interaction


def create_interaction(db: Session, data: dict):

    interaction = Interaction(
        doctor_name=data.get("doctor_name"),
        hospital=data.get("hospital"),
        speciality=data.get("speciality") or "Unknown",
        interaction_type=data.get("interaction_type") or "AI Chat",
        discussion=data.get("discussion"),
        products=", ".join(data.get("products", []))
        if isinstance(data.get("products"), list)
        else data.get("products"),
        next_followup=data.get("next_followup"),
        summary=data.get("summary"),
    )

    db.add(interaction)
    db.commit()
    db.refresh(interaction)

    return interaction


def get_all_interactions(db: Session):
    return db.query(Interaction).order_by(Interaction.id.desc()).all()


def get_interaction(db: Session, interaction_id: int):
    return (
        db.query(Interaction)
        .filter(Interaction.id == interaction_id)
        .first()
    )


def update_interaction(db: Session, interaction_id: int, data: dict):

    interaction = get_interaction(db, interaction_id)

    if not interaction:
        return None

    for key, value in data.items():
        setattr(interaction, key, value)

    db.commit()
    db.refresh(interaction)

    return interaction


def delete_interaction(db: Session, interaction_id: int):

    interaction = get_interaction(db, interaction_id)

    if not interaction:
        return None

    db.delete(interaction)
    db.commit()

    return True


def search_interactions(db: Session, query: str):

    return (
        db.query(Interaction)
        .filter(
            or_(
                Interaction.doctor_name.ilike(f"%{query}%"),
                Interaction.hospital.ilike(f"%{query}%"),
                Interaction.speciality.ilike(f"%{query}%"),
                Interaction.products.ilike(f"%{query}%"),
                Interaction.summary.ilike(f"%{query}%"),
            )
        )
        .all()
    )