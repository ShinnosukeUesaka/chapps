from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Milvus
from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import CharacterTextSplitter

from langchain.document_loaders import TextLoader

# Use the WebBaseLoader to load specified web pages into documents

loader = TextLoader("chapps/dashboard.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
# Split the documents into smaller chunks
text_splitter = CharacterTextSplitter(chunk_size=1024, chunk_overlap=0)
docs = text_splitter.split_documents(documents)


embeddings = OpenAIEmbeddings()

# Set up a vector store used to save the vector embeddings. Here we use Milvus as the vector store.
vector_store = Milvus.from_documents(
    docs,
    embedding=embeddings,
    connection_args={"uri": "https://in03-e111341672d43e4.api.gcp-us-west1.zillizcloud.com", "token": "6adfa49407c02797f742bba3b5be591048ec44da1181f4f1bb7daf5482a5407fb2dc0585c8dac4e5f0ec679d2ea5b6eef0bdfd01"}
)
