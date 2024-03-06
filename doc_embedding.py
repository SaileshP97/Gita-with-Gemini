import os

import pymongo
from dotenv import load_dotenv

from get_data import get_df

from sentence_transformers import SentenceTransformer

load_dotenv()

# https://huggingface.co/thenlper/gte-large
embedding_model = SentenceTransformer("thenlper/gte-large")


def get_embedding(text: str) -> list[float]:
    if not text.strip():
        print("Attempted to get embedding for empty text.")
        return []

    embedding = embedding_model.encode(text)

    return embedding.tolist()


def get_mongo_client():
    """Establish connection to the MongoDB."""

    mongo_uri = (
        f"mongodb+srv://{os.environ['USERNAME']}:{os.environ['Password']}"
        "@vec-embedding.hppejw9.mongodb.net/"
    )

    print(mongo_uri)

    try:
        client = pymongo.MongoClient(mongo_uri)
        print("Connection to MongoDB successful")
        return client
    except pymongo.errors.ConnectionFailure as e:
        print(f"Connection failed: {e}")
        return None


if __name__ == "__main__":
    gita_df = get_df()
    gita_df["embedding"] = gita_df["text"].apply(get_embedding)

    mongo_client = get_mongo_client()
    db = mongo_client["gita"]
    collection = db["gita_collection"]

    collection.delete_many({})

    documents = gita_df.to_dict("records")
    collection.insert_many(documents)
    print("Embedding Collection Succesfully uploaded to MongoDB...")
