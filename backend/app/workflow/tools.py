# app/application/tools/movie_retriever_tool.py

from langchain_core.tools import create_retriever_tool
from vector_store import get_chroma_vector_store

def get_movie_retriever_tool():
    """Create and return the movie retriever tool"""
    return create_retriever_tool(
        retriever=get_chroma_vector_store(),
        name="movie_retriever_tool",
        description="A tool that can retrieve information from the vector store about movies. Use this when you need to search for specific movies or movie information."
    )




