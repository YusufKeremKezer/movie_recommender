from workflow.state import UserState
from workflow.chains import get_conversation_summary_chain, get_movie_recommendation_chain
from langchain_core.messages import RemoveMessage, SystemMessage
from config import settings
from langgraph.prebuilt import ToolNode
from workflow.tools import get_movie_retriever_tool

async def summarize_conversation_node(state: UserState) -> UserState:
    summary = state.get("summary", "")
    summary_chain = await get_conversation_summary_chain(summary)

    # The user's last message is the most recent one
    user_message = state["messages"][-1].content

    response = await summary_chain.ainvoke(
        {
            "messages": state["messages"],
            "user_message": user_message,
            "summary": summary,
        }
    )

    delete_messages = [
        RemoveMessage(id=m.id)
        for m in state["messages"][: -settings.TOTAL_MESSAGES_AFTER_SUMMARY]
    ]
    return {"summary": response.content, "messages": delete_messages}


async def recommendation_node(state: UserState) -> dict:
    """
    Generates a movie recommendation based on the user's conversation history and summary.
    """
    summary = state.get("summary")
    messages = state["messages"]

    chain_messages = []
    if summary:
        chain_messages.append(
            SystemMessage(
                f"Here is a summary of the conversation so far:\n{summary}"
            )
        )

    chain_messages.extend(messages)

    recommendation_chain = await get_movie_recommendation_chain()
    response = await recommendation_chain.ainvoke({"messages": chain_messages})
    return {"messages": [response]}

retriever_tool = ToolNode([get_movie_retriever_tool()])
