import json
from app.services.llm import llm


def summarize_interaction(text: str):
    prompt = f"""
You are an AI CRM assistant.

The user must provide ONLY ONE doctor interaction.

If multiple doctor visits are mentioned,
extract ONLY THE FIRST doctor interaction.

Return ONLY valid JSON.

Do NOT explain.
Do NOT add any text before the JSON.
Do NOT wrap the JSON inside markdown.
Output must start with {{ and end with }}.

Schema:

{{
    "doctor_name":"",
    "hospital":"",
    "speciality":"",
    "products":[],
    "summary":"",
    "next_followup":""
}}

Interaction:

{text}
"""

    response = llm.invoke(prompt)

    content = response.content.strip()

    # Remove markdown if present
    content = content.replace("```json", "")
    content = content.replace("```", "")
    content = content.strip()

    print("\n========== LLM RESPONSE ==========")
    print(content)
    print("==================================\n")

    # Extract only JSON
    start = content.find("{")
    end = content.rfind("}")

    if start == -1 or end == -1:
        raise Exception("No valid JSON returned from AI.")

    json_text = content[start:end + 1]

    return json.loads(json_text)