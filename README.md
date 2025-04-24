# KnotebookLM RAG Service

Knotebook LM is a system which helps in summarizing information throught a RAG(Retrieval-Augmented-Generation) service. This allows more relevant information generation, and accurate outputs. You are able to create new notebooks, add sources to the notebook, and explore new ideas!

This involves the use of a Google Embeddings and a Flask API as well as LangChain's database to split, embed, and store a set of text, offering a summary of information through all of these working together with each other. Keep in mind that this is in openeing stages, and I am also having this be a school project for coding class.

This is inspired by Google's NotebookLM.

# Operating Instructions

1. Delete the text within the "test_text" variable within the "text_split.py" file.
2. Run the "api.py" file within the terminal window.
3. On another terminal window, run the "post.py" file, which would be able to run the post request for you.
4. Once your post is created, your text will be turned into embedding ID's, and will be displayed in a list for you.

# Conclusion

Overall, I hope that you will enjoy the code I have created. Even though it may be basic, I worked very hard on it with my limited knowledge of coding. Nevertheless, you at least attempting to use it would make my day!