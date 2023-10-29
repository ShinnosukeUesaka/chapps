from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Milvus
from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import CharacterTextSplitter

from langchain.document_loaders import TextLoader
from langchain.document_loaders import PyPDFLoader
import os


# Use the WebBaseLoader to load specified web pages into documents

def create_embedding(collection_name: str, pdf_path: str):
    loader = PyPDFLoader(pdf_path)
    text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=0)
    pages = loader.load_and_split(text_splitter)

    embeddings = OpenAIEmbeddings()

    # Set up a vector store used to save the vector embeddings. Here we use Milvus as the vector store.
    vector_store = Milvus.from_documents(
        pages,
        embedding=embeddings,
        collection_name=collection_name,
        connection_args={"uri": "https://in03-e111341672d43e4.api.gcp-us-west1.zillizcloud.com", "token": os.environ["DB_TOKEN"]},
    )

def get_related_text(collection_name: str, prompt: str) -> str:
    embeddings = OpenAIEmbeddings()
    vector_store = Milvus.from_connection(
        collection_name=collection_name,
        embedding=embeddings,
        connection_args={"uri": "https://in03-e111341672d43e4.api.gcp-us-west1.zillizcloud.com", "token": os.environ["DB_TOKEN"]},
    )

    # Get the text that is most related to the prompt
    related_text = vector_store.similarity_search(prompt)[0].page_content
    return related_text
