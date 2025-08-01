from config import settings
from typing import Literal
from workflow.state import UserInteractionState
from langgraph.graph import END

def should_summarize_conversation(
    state: UserInteractionState,
) -> Literal["summarize_conversation_node", END]:
    messages = state["messages"]

    if len(messages) > settings.TOTAL_MESSAGES_SUMMARY_TRIGGER:
        return "summarize_conversation_node"

    return END

def should_use_wikipedia(
    state: UserInteractionState,
) -> Literal["wikipedia_node", END]:
    messages = state["messages"]

    if len(messages) > settings.TOTAL_MESSAGES_SUMMARY_TRIGGER:
        return "summarize_conversation_node"

    return END
