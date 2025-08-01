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


def create_workflow_graph():
    """Create the langgraph workflow graph"""
    graph = StateGraph(UserInteractionState)

    # Add nodes
    graph.add_node("summarize_conversation_node", summarize_conversation_node)
    graph.add_node("conversation_node", conversation_node)
    graph.add_node("connector_node", connector_node)
    graph.add_node("retriever_node", retriever_node)
    


    graph.add_edge(START,"conversation_node")
    graph.add_conditional_edges(
        "conversation_node",
        tools_condition,
        {
            "tools": "retriever_node",
            END: "connector_node"
        }
    )
    graph.add_edge("retriever_node", "conversation_node")
    graph.add_conditional_edges("connector_node", should_summarize_conversation)
    graph.add_edge("summarize_conversation_node", END)

    return graph.compile()


if __name__ == "__main__":
    graph = create_workflow_graph()
    response = graph.invoke({"messages": [HumanMessage(content="Hello, recommend me a comedy movie?")],"summary":""})
    print(response)


