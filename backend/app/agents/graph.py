from langgraph.prebuilt import create_react_agent

from app.services.llm import llm
from app.services.tools import (
    log_interaction,
    edit_interaction,
    search_interaction,
    generate_followup,
    recommend_next_visit,
)

agent = create_react_agent(
    model=llm,
    tools=[
        log_interaction,
        edit_interaction,
        search_interaction,
        generate_followup,
        recommend_next_visit,
    ],
    prompt="""
You are an AI CRM assistant for pharmaceutical sales representatives.

Available tools:

- log_interaction
- edit_interaction
- search_interaction
- generate_followup
- recommend_next_visit

Always use the appropriate tool when required.
"""
)