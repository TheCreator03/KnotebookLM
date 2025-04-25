from split import split_text
from embed_and_store import add_documents

test_text = "Hello, my name is Vincent Krause, please embed this so I can finish my CS project and not get a zero."

user_id = '321'
document_id = '12345'
splits = split_text(test_text, user_id, document_id)
for split in splits:
    print (split.page_content[:50], split.metadata)

vector_ids = add_documents(splits)
# Example user and document ID, uses the "split_text" definition to print the page out/