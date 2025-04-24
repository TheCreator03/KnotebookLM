from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def split_text(text, user_id, document_id, notebook_id):
    doc = Document(page_content=text, metadata={ "user_id": user_id, "document_id": document_id, "notebook_id": notebook_id })
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=200, add_start_index=True)
    splits = text_splitter.split_documents([doc])
    return splits
# Pretty self-explanatory: it takes all of the identifications and puts them into onw variable, then splits the text into chunks and returns the split text.