from langchain_chroma.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings  # Use LangChain's embedding

# Use LangChain's HuggingFace embeddings instead
embedding_function = HuggingFaceEmbeddings(
    model_name="Alibaba-NLP/gte-multilingual-base",
    model_kwargs={'trust_remote_code': True}
)

vector_store = Chroma(
    collection_name="imdb_data",
    persist_directory="long_term_memory/",
    embedding_function=embedding_function  # Use the LangChain embedding
)
def get_chroma_retriever():
    return vector_store.as_retriever()

if __name__ == "__main__":
    print(get_chroma_retriever().invoke("turkish history"))
