from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from workflow.tools import tools
from domain.prompts import (
    SUMMARY_PROMPT,
    EXTEND_SUMMARY_PROMPT,
    IMDB_EXPERT_CARD,
    )
from langchain_core.messages import HumanMessage
import asyncio
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

async def get_response_chain():
    model = get_chat_model()
    model = model.bind_tools(tools)
    system_message = IMDB_EXPERT_CARD

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

async def main():
    chain = await get_response_chain()
    response = await chain.ainvoke({"messages": [HumanMessage(content="Hello, recommend me a comedy movie?")], "summary": ""})
    print(response.content)


if __name__ == "__main__":
    asyncio.run(main())