from langgraph.graph import MessagesState
from pydantic import Field

class UserState(MessagesState):
    """State for LLM-driven movie recommendation workflow using vector store"""
    summary: str = Field("", description="The summary of the conversation between the user and the AI assistant")   
    
