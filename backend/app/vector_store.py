from langchain_chroma.vectorstores import Chroma
from chromadb.utils import embedding_functions

vector_store = Chroma(
    collection_name="imdb_data",
    persist_directory= "long_term_memory/",
    embedding_function=embedding_functions.SentenceTransformerEmbeddingFunction(model_name="Alibaba-NLP/gte-multilingual-base",trust_remote_code=True)
)

def get_chroma_vector_store():
    return vector_store.as_retriever()


if __name__ == "__main__":
    print(get_chroma_vector_store().invoke("High imdb rating movie that engaging"))
