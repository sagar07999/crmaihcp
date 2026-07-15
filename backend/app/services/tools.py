from langchain_core.tools import tool

from sqlalchemy.orm import Session

from app.models import Interaction
from app.services.ai_service import summarize_interaction


def log_ai_interaction(text: str, db: Session):

    data = summarize_interaction(text)

    interaction = Interaction(
        doctor_name=data["doctor_name"],
        hospital=data["hospital"],
        speciality=data["speciality"] or "Unknown",
        interaction_type="AI Chat",
        discussion=text,
        products=", ".join(data["products"]),
        next_followup=None,
        summary=data["summary"]
    )

    db.add(interaction)
    db.commit()
    db.refresh(interaction)

    return interaction
@tool
def log_interaction(interaction: str):
    """
    Log a new doctor interaction.
    """
    return f"Interaction logged successfully: {interaction}"


@tool
def edit_interaction(interaction_id: int, updated_text: str):
    """
    Edit an existing interaction.
    """
    return f"Interaction {interaction_id} updated."


@tool
def search_interaction(query: str):
    """
    Search previous doctor interactions.
    """
    return f"Searching interactions for '{query}'."


@tool
def generate_followup(summary: str):
    """
    Generate follow-up message.
    """
    return f"Follow-up generated for: {summary}"


@tool
def recommend_next_visit(speciality: str):
    """
    Recommend next visit plan.
    """
    return f"Recommended next visit strategy for {speciality}."