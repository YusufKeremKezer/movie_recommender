from langchain_chroma.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings  

# Alibaba-NLP
embedding_function = HuggingFaceEmbeddings(
    model_name="intfloat/multilingual-e5-base",
    model_kwargs={'trust_remote_code': True}
)

vector_store = Chroma(
    collection_name="imdb_data",
    persist_directory="long_term_memory/",
    embedding_function=embedding_function  
)
def get_chroma_retriever():
    return vector_store.as_retriever()

if __name__ == "__main__":
    print(get_chroma_retriever().invoke("turkish history"))
