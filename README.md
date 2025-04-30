# KnotebookLM RAG Service

Knotebook LM is a system which helps in summarizing information throught a RAG(Retrieval-Augmented-Generation) service. This allows more relevant information generation, and accurate outputs. You are able to create new notebooks, add sources to the notebook, and explore new ideas! So if you want to make embeddings with text you provide, this is perfect for that kind of job!

This involves the use of a Google Embeddings and a Flask API as well as LangChain's database to split, embed, and store a set of text, offering a summary of information through all of these working together with each other. Keep in mind that this is in opening stages, and I am also having this be a school project for coding class.

This is inspired by Google's NotebookLM.

# Operating Instructions

1. Delete the text within the "test_text" variable within the "text_split.py" file.
2. Run the "api.py" file within the terminal window.
3. On another terminal window, run the "post.py" file, which would be able to run the post request for you.
4. Once your post is created, your text will be turned into embedding ID's, and will be displayed in a list for you.

# Environmental Variables

The most common variables would be the chunk sizes. You can change these by heading over to "split.py" and change the chunk size for how many characters you want in a single chunk, the chunk overlap for how much of the last chunk the current chunk takes up, and adding a start index if you want.

In regards to handling the API key, just let the API key handle itself. I'm not giving you it. >:(

# Making Requests

1. Follow the operating instructions stated above.
2. Operate "post.py".
3. From the url given, add "/new" to the end.
4. When running POST on the terminal, a successful request should pop up.

# Example of a Error Request

Following the operating instructions and then operating the url without adding "/new" to it.

# Example of a Good Request

Stated above in "Making Requests".

# Installations

1. Google API
    From the terminal, write "pip install google-genai"
2. Flask API
    From the terminal, write "pip install Flask"
3. LangChain
    From the terminal, write "pip install langchain"
4. Chroma
    From the terminal, "write pip install -qU "langchain-chroma>=0.1.2""

# Conclusion

Overall, I hope that you will enjoy the code I have created. Even though it may be basic, I worked very hard on it with my limited knowledge of coding. Nevertheless, you at least attempting to use it would make my day!

# Links to More Information/Documentation

Google API: https://cloud.google.com/ai/generative-ai?hl=en
Flask API: https://flask.palletsprojects.com/en/stable/api/
LangChain: https://python.langchain.com/api_reference/
Chroma: https://python.langchain.com/docs/integrations/vectorstores/chroma/

Hope this helps!
