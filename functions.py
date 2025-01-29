from sentence_transformers import SentenceTransformer
import chromadb
import json
import os
from chromadb.config import Settings
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

# Initialize ChromaDB client
chroma_client = chromadb.PersistentClient(
    path="vector_store",
    settings=Settings(persist_directory="vector_store")
)

# Load ChromaDB collection
collection = chroma_client.get_or_create_collection(name="disease_embeddings")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

GROQ_API_KEY=os.environ.get("GROQ_API_KEY")

# Load dataset
with open("Disease_Symptoms_3.json", "r") as file:
    data = json.load(file)

def query_disease_symptoms(user_input):
    """
    Query ChromaDB for diseases based on the user input symptoms.
    """
    query_embedding = model.encode(user_input)
    results = collection.query(query_embeddings=[query_embedding], n_results=5)

    # Display the results
    for i, result in enumerate(results["documents"][0]):
        disease = results["metadatas"][0][i]["disease"]
        # return f"{i+1}. Disease: {disease} | Symptoms: {result}"
        return f"{disease}"

def get_response_from_groq(user_query, disease_info):
    if not disease_info:
        return "Sorry, no relevant disease information found."

    full_context = f"User symptoms: {user_query}\nPredicted disease: {disease_info}\nProvide medical advice."

    groq_api = GROQ_API_KEY
    llm = ChatGroq(groq_api_key=groq_api, model_name="Llama3-8b-8192")

    response = llm.invoke(full_context)
    return response.content if response else "No response from the AI."
