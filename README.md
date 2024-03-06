### Gita-with-Gemini is a project aimed at implementing a Real-Time Answer Generation (RAG) application using document embedding and retrieval techniques for a domain-based chat system centered around the Bhagavad Gita. The project involves the following key steps:

## Data Collection and Preprocessing:

Raw text data from the Bhagavad Gita's purport was obtained from [Vedabase](https://vedabase.io/en/).
The text underwent preprocessing and was stored in a structured format within a DataFrame.
## Text Embedding:

Utilized the "thenlper/gte-large" model from the sentence_transformers library for embedding the textual data. This step facilitated efficient representation of the text in a high-dimensional vector space.
## Data Storage and Retrieval:

Leveraged MongoDB's cloud-based collection for storing and retrieving data based on cosine similarity. This allowed for effective management and retrieval of relevant information during the chat process.
## Response Generation:

Created a response generation model using Google's Gemini Pro model through the google-generativeai library and API.
By passing the context and query to the model, the system generates appropriate responses tailored to the user's inquiries within the domain of the Bhagavad Gita.
## Web Interface

Implemented a user-friendly web interface using Gradio for seamless interaction with the chat system. Gradio simplifies the process of deploying machine learning models as interactive web applications, enhancing accessibility and usability for users.

### This project aims to offer a seamless and interactive chat experience for users seeking insights and information related to the Bhagavad Gita, utilizing advanced techniques in natural language processing and machine learning.

### Screenshots:

![Screenshot 1](path/to/screenshot1.png)
*Caption for screenshot 1*

![Screenshot 2](path/to/screenshot2.png)
*Caption for screenshot 2*
