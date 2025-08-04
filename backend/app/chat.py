import asyncio
from langchain_core.messages import HumanMessage, AIMessage
from workflow.graph import create_workflow_graph

async def get_ai_response(user_input, chat_history):
    """Get the AI's response to a user's message."""
    graph = create_workflow_graph()

    # Convert the chat history to the expected format
    messages = []
    for msg in chat_history:
        if msg["role"] == "user":
            messages.append(HumanMessage(content=msg["content"]))
        else:
            messages.append(AIMessage(content=msg["content"]))

    state = {"messages": messages, "summary": ""}
    state["messages"].append(HumanMessage(content=user_input))
    
    result = await graph.ainvoke(state)
    return result["messages"][-1].content


if __name__ == "__main__":
    asyncio.run(chat_with_graph())
