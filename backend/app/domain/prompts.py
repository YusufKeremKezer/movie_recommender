import logging

logger = logging.getLogger(__name__)

class Prompt:
    def __init__(self, name: str, prompt: str) -> None:
        self.name = name
        self.__prompt = prompt

    @property
    def prompt(self) -> str:
        return self.__prompt

    def __str__(self) -> str:
        return self.prompt


__SUMMARY_PROMPT = """Create a comprehensive summary of the conversation between the user and AI assistant that includes all movie preferences mentioned.

User: {user_message}
Context: {conversation_context}

The summary must be a short description of the conversation so far, but that also captures all the relevant information shared between the user and the AI assistant, specifically including any movie preferences such as:
- Preferred genres
- Year preferences  
- Rating preferences
- Favorite directors
- Keywords or themes mentioned
- Specific movies referenced

Make sure to naturally incorporate these movie preference details within the summary narrative."""

SUMMARY_PROMPT = Prompt(
    name="summary",
    prompt=__SUMMARY_PROMPT,
)



__EXTEND_SUMMARY_PROMPT = """This is summary conversation between the user and Assistant 
{summary}.

Extend the summary by taking into account the new messages above: """

EXTEND_SUMMARY_PROMPT = Prompt(
    name="extend_summary",
    prompt=__EXTEND_SUMMARY_PROMPT,
)

__GENERATE_RECOMMENDATIONS_PROMPT = """Generate movie recommendations based on the conversation.

Recommendations:
"""

GENERATE_RECOMMENDATIONS_PROMPT = Prompt(
    name="generate_recommendations",
    prompt=__GENERATE_RECOMMENDATIONS_PROMPT,
)
