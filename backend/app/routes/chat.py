from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.ai_service import summarize_interaction
from app.services.tools import log_ai_interaction
from app.crud import search_interactions

router = APIRouter(
    prefix="/chat",
    tags=["AI Chat"]
)


class ChatRequest(BaseModel):
    input: str


GREETINGS = [
    "hi",
    "hello",
    "hey",
    "good morning",
    "good afternoon",
    "good evening",
    "how are you",
]


@router.post("/")
def chat(request: ChatRequest, db: Session = Depends(get_db)):
    try:

        user_input = request.input.strip()
        lower = user_input.lower()

        # Empty input
        if not user_input:
            return {
                "message": "Please enter your doctor interaction."
            }

        # Greeting
        if lower in GREETINGS:
            return {
                "message": """👋 Hello!

I'm your AI CRM Assistant.

I can help you:

✅ Log doctor interactions
✅ Search previous interactions
✅ Generate summaries
✅ Generate follow-up suggestions
✅ Recommend next visit plans

Please describe your interaction or ask me a question."""
            }

        # ---------------- SEARCH ----------------

        if "search" in lower or "show" in lower or "find" in lower:

            query = user_input

            for word in [
                "show",
                "search",
                "find",
                "interaction",
                "interactions",
            ]:
                query = query.replace(word, "")
                query = query.replace(word.capitalize(), "")

            query = query.strip()

            results = search_interactions(db, query)

            if not results:
                return {
                    "message": f"No interactions found for '{query}'."
                }

            msg = "🔍 Matching Interactions\n\n"

            for item in results:
                msg += (
                    f"👨‍⚕️ Doctor: {item.doctor_name}\n"
                    f"🏥 Hospital: {item.hospital}\n"
                    f"🩺 Speciality: {item.speciality}\n"
                    f"💊 Products: {item.products}\n"
                    f"📝 Summary: {item.summary}\n"
                    "----------------------------------\n"
                )

            return {"message": msg}

        # ---------------- FOLLOW-UP ----------------

        if "follow-up" in lower or "follow up" in lower:

            return {
                "message":
                """📅 Suggested Follow-up

• Share requested clinical studies.
• Provide product brochures.
• Discuss patient outcomes.
• Schedule next visit within 1-2 weeks.
• Capture doctor's prescribing feedback."""
            }

        # ---------------- NEXT VISIT ----------------

        if "next visit" in lower or "recommend" in lower:

            return {
                "message":
                """📌 Next Visit Recommendation

• Review previous discussion.
• Bring latest clinical evidence.
• Compare competitor products.
• Address doctor's concerns.
• Record feedback in CRM."""
            }

        # ---------------- LOG INTERACTION ----------------

        data = summarize_interaction(user_input)

        if (
            not data.get("doctor_name")
            and not data.get("hospital")
            and not data.get("summary")
        ):
            return {
                "message":
                "I couldn't identify a doctor interaction. Please provide doctor name, hospital, products discussed, etc."
            }

        interaction = log_ai_interaction(
            user_input,
            db
        )

        return {
            "message": f"""✅ Interaction Logged Successfully

👨‍⚕️ Doctor : {interaction.doctor_name}

🏥 Hospital : {interaction.hospital}

🩺 Speciality : {interaction.speciality}

💊 Products : {interaction.products}

📝 Summary :
{interaction.summary}

📅 Follow-up :
{data.get("next_followup") or "Not specified"}
""",
            "interaction": {
                "id": interaction.id,
                "doctor_name": interaction.doctor_name,
                "hospital": interaction.hospital,
                "speciality": interaction.speciality,
                "products": interaction.products,
                "summary": interaction.summary,
            },
        }

    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )