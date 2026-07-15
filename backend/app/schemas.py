from pydantic import BaseModel, ConfigDict
from datetime import date


class InteractionBase(BaseModel):
    doctor_name: str | None = None
    hospital: str | None = None
    speciality: str | None = None
    interaction_type: str | None = None
    discussion: str | None = None
    products: str | None = None
    next_followup: date | None = None
    summary: str | None = None


class InteractionCreate(InteractionBase):
    pass


class InteractionResponse(InteractionBase):
    id: int

    model_config = ConfigDict(from_attributes=True)