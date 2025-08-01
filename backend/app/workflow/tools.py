# app/application/tools/movie_retriever_tool.py

from langchain_core.tools import create_retriever_tool
from vector_store import get_chroma_retriever
from langchain_community.retrievers import WikipediaRetriever

retriever_tool = create_retriever_tool(
        retriever=get_chroma_retriever(),
        name="movie_retriever_tool",
        description=" Search the vector store for movies and tv series. Always use this tool when the user asks you about recommendation for a movie or tv series"
    )

wikipedia_tool = create_retriever_tool(
        retriever=WikipediaRetriever(kwargs={"top_k": 1}),
        name="wikipedia_tool",
        description="Search the wikipedia for related movie or tv series. Always use this tool when the user asks you about further information about a movie or tv series"
    )


tools = [retriever_tool, wikipedia_tool]

