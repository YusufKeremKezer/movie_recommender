from workflow.state import UserInteractionState
from workflow.chains import get_conversation_summary_chain, get_response_chain
from langchain_core.messages import RemoveMessage
from config import settings
from langgraph.prebuilt import ToolNode
from workflow.tools import tools

async def summarize_conversation_node(state: UserInteractionState) -> UserInteractionState:
    summary = state.get("summary", "")
    summary_chain = await get_conversation_summary_chain(summary)

    response = await summary_chain.ainvoke(
        {
            "messages": state["messages"],
            "summary": summary,
        }
    )

    delete_messages = [
        RemoveMessage(id=m.id)
        for m in state["messages"][: -settings.TOTAL_MESSAGES_AFTER_SUMMARY]
    ]
    return {"summary": response.content, "messages": delete_messages}


async def conversation_node(state: UserInteractionState) -> UserInteractionState:
    summary = state.get("summary", "")
    response_chain = await get_response_chain()
    response = await response_chain.ainvoke(
        {
            "messages": state["messages"],
            "summary": summary,
        }
    )
    return {"messages": [response]}

async def connector_node(state: UserInteractionState) -> UserInteractionState:
    return {}


retriever_node = ToolNode(tools)

