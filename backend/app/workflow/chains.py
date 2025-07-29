from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from workflow.tools import get_movie_retriever_tool
from domain.prompts import (
    GENERATE_RECOMMENDATIONS_PROMPT,
    SUMMARY_PROMPT,
    EXTEND_SUMMARY_PROMPT,
)
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

def get_chat_model():
    """Initializes and returns the ChatGoogleGenerativeAI model, ensuring the API key is passed explicitly."""
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in environment variables.")
    return ChatGoogleGenerativeAI(
        model="gemini-2.0-flash", temperature=0.7, google_api_key=api_key
    )


async def get_movie_recommendation_chain():
    model = get_chat_model()
    model = model.bind_tools([get_movie_retriever_tool()])
    system_message = GENERATE_RECOMMENDATIONS_PROMPT

    prompt = ChatPromptTemplate.from_messages(
        [
        ("system", system_message.prompt),
        MessagesPlaceholder(variable_name="messages"),
    ],
    )
    return prompt | model


async def get_conversation_summary_chain(summary:str = ""):
    model = get_chat_model()
    summary_message = EXTEND_SUMMARY_PROMPT if summary else SUMMARY_PROMPT
    prompt = ChatPromptTemplate.from_messages(
        [
        MessagesPlaceholder(variable_name="messages"),
        ("human", summary_message.prompt),
    ],
    )
    return prompt | model