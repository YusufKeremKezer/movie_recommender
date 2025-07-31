from langgraph.graph import StateGraph, START, END
from workflow.state import UserInteractionState
from workflow.nodes import (
    conversation_node,
    summarize_conversation_node,
    retriever_node,
)
from langgraph.prebuilt import tools_condition
from workflow.nodes import connector_node
from workflow.edges import should_summarize_conversation
from langchain_core.messages import HumanMessage
import asyncio



def create_workflow_graph():
    """Create the langgraph workflow graph"""
    graph = StateGraph(UserInteractionState)

    # Add nodes
    graph.add_node("summarize_conversation_node", summarize_conversation_node)
    graph.add_node("conversation_node", conversation_node)
    graph.add_node("recommendation_retriever_node", retriever_node)
    graph.add_node("connector_node", connector_node)
    graph.add_conditional_edges(
        "conversation_node",
        tools_condition,
        {
            "tools": "recommendation_retriever_node",
            END: "connector_node"
        }
    )
    graph.add_edge(START,"conversation_node")
    graph.add_edge("recommendation_retriever_node", "conversation_node")
    graph.add_conditional_edges("connector_node", should_summarize_conversation)
    graph.add_edge("summarize_conversation_node", END)

    return graph.compile()


async def chat_with_graph():
    """Interactive conversation with the graph"""
    graph = create_workflow_graph()
    print(graph.get_graph().draw_ascii())

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
