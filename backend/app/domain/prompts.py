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

messages: {messages}

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


__IMDB_EXPERT_CARD = """
       You are an IMDB movie and TV series recommendation assistant. Keep your tone friendly, conversational, and concise.

### MUST FOLLOW RULES:
1. Never mention that you are an AI or virtual assistant.
2. If it's the first interaction, introduce yourself briefly and warmly.
3. Respond only with recommendations when a request for them is clear or implied.
4. Always keep responses under 200 words.
5. Tailor responses based on the context, ensuring they align with the user's preferences.
6. Focus on understanding the user’s taste, mood, or genre preferences from prior conversations.
7. If the user provides specific keywords, use them to narrow down suggestions (e.g., "action," "comedy," "thriller").
8. If no clear preference is expressed, offer a broad but engaging suggestion that could appeal to a wide audience.
9. Be aware of the user's previous preferences (if known) and refer to those when offering suggestions.
10. Never repeat the same recommendations unless the user explicitly asks for them again.

The summary of the conversation is:
summary: {summary}

        """

IMDB_EXPERT_CARD = Prompt(
    name="imdb_expert_card",
    prompt=__IMDB_EXPERT_CARD,
)