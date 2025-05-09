__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
# Imports SQLite3.

from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model='models/text-embedding-004')
vector_store = Chroma(
    collection_name='knotebooklm',
    embedding_function=embeddings,
    persist_directory='./chroma_langchain_db',
)
# Embeddings and vector stores created through Google GenAI and Chroma DB.

def add_documents(purple_monkey_dishwasher_for_vincent):
    return vector_store.add_documents(documents=purple_monkey_dishwasher_for_vincent)
# Defines where the vector store would add documents.