from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Interaction
from app.schemas import InteractionCreate, InteractionResponse

router = APIRouter(prefix="/interactions", tags=["Interactions"])


# Create Interaction
@router.post("/", response_model=InteractionResponse)
def create_interaction(data: InteractionCreate, db: Session = Depends(get_db)):
    interaction = Interaction(**data.model_dump())
    db.add(interaction)
    db.commit()
    db.refresh(interaction)
    return interaction


# Get All Interactions
@router.get("/", response_model=list[InteractionResponse])
def get_interactions(db: Session = Depends(get_db)):
    return db.query(Interaction).all()


# Get Single Interaction
@router.get("/{interaction_id}", response_model=InteractionResponse)
def get_interaction(interaction_id: int, db: Session = Depends(get_db)):
    interaction = db.query(Interaction).filter(
        Interaction.id == interaction_id
    ).first()

    if not interaction:
        raise HTTPException(status_code=404, detail="Interaction not found")

    return interaction


# Update Interaction
@router.put("/{interaction_id}", response_model=InteractionResponse)
def update_interaction(
    interaction_id: int,
    data: InteractionCreate,
    db: Session = Depends(get_db)
):
    interaction = db.query(Interaction).filter(
        Interaction.id == interaction_id
    ).first()

    if not interaction:
        raise HTTPException(status_code=404, detail="Interaction not found")

    for key, value in data.model_dump().items():
        setattr(interaction, key, value)

    db.commit()
    db.refresh(interaction)

    return interaction


# Delete Interaction
@router.delete("/{interaction_id}")
def delete_interaction(interaction_id: int, db: Session = Depends(get_db)):
    interaction = db.query(Interaction).filter(
        Interaction.id == interaction_id
    ).first()

    if not interaction:
        raise HTTPException(status_code=404, detail="Interaction not found")

    db.delete(interaction)
    db.commit()

    return {"message": "Interaction deleted successfully"}