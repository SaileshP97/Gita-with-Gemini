import os

import google.generativeai as genai
import gradio as gr

from doc_embedding import get_embedding, get_mongo_client


def vector_search(user_query, collection):
    query_embedding = get_embedding(user_query)

    if query_embedding is None:
        return "Invalid query or embedding generation failed."

    # Define the vector search pipeline
    pipeline = [
        {
            "$vectorSearch": {
                "index": "vector_index",
                "queryVector": query_embedding,
                "path": "embedding",
                "numCandidates": 150,
                "limit": 4,
            }
        },
        {
            "$project": {
                "_id": 0,
                "text": 1,
                "embedding": 1,
                "score": {"$meta": "vectorSearchScore"},
            }
        },
    ]

    # Execute the search
    results = collection.aggregate(pipeline)
    return list(results)


def get_search_result(query, collection):
    get_knowledge = vector_search(query, collection)

    search_result = ""
    for result in get_knowledge:
        search_result += f"Text: {result.get('text', 'N/A')}\n"

    return search_result


def generate_text(input_text, history):
    source_information = get_search_result(input_text, collection)
    combined_information = f"""Query: {input_text}\nContinue to answer
    the query by using the Search Results:\n{source_information}."""

    response = model.generate_content(combined_information)

    return response.text


if __name__ == "__main__":
    mongo_client = get_mongo_client()
    db = mongo_client["gita"]
    collection = db["gita_collection"]

    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
    model = genai.GenerativeModel("gemini-pro")

    iface = gr.ChatInterface(fn=generate_text, title="Chat with Assistant")
    iface.launch(share=False, server_port=2020)
