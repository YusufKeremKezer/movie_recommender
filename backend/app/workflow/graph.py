from langgraph.graph import StateGraph, START, END
from workflow.state import UserState
from workflow.nodes import (
    summarize_conversation_node,
    recommendation_node,
)
from workflow.edges import should_extend_summary
from langchain_core.messages import HumanMessage
import asyncio
from langgraph.prebuilt import ToolNode
from app.workflow.tools import get_movie_retriever_tool


def create_workflow_graph():
    """Create the langgraph workflow graph"""
    workflow = StateGraph(UserState)

    # Add nodes
    workflow.add_node("summarize_conversation", summarize_conversation_node)
    workflow.add_node("recommendation", recommendation_node)
    workflow.add_node("tools", ToolNode([get_movie_retriever_tool()]))

    # Add edges
    workflow.add_conditional_edges(
        "summarize_conversation",
        should_extend_summary,
        {
            "extend_summary": "summarize_conversation",
            "summary": "recommendation",
        },
    )
    
    workflow.add_conditional_edges(
        "recommendation",
        should_call_tools,
        {
            "tools": "tools",
            "end": END,
        },
    )
    
    workflow.add_edge("tools", "recommendation")
    workflow.set_entry_point("summarize_conversation")

    return workflow.compile()


async def chat_with_graph():
    """Interactive conversation with the graph"""
    graph = create_workflow_graph()
    state = {"messages": [], "summary": ""}
    
    print("Movie Recommender Chat (type 'quit' to exit)")
    print("-" * 40)
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['quit', 'exit', 'q']:
            break
            
        # Add user message to state
        state["messages"].append(HumanMessage(content=user_input))
        
        # Run the graph
        result = await graph.ainvoke(state)
        
        # Update state with result
        state.update(result)
        
        # Print AI response
        if result.get("messages"):
            ai_message = result["messages"][-1]
            print(f"AI: {ai_message.content}")


if __name__ == "__main__":
    asyncio.run(chat_with_graph())