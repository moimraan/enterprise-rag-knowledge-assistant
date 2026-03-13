from fastapi import FastAPI
from pydantic import BaseModel
from retrieval.vector_index import VectorIndex
from llm_pipeline.rag_pipeline import RAGPipeline
from embeddings.embedding_generator import EmbeddingGenerator

app = FastAPI()

embedder = EmbeddingGenerator()

documents = [
    "Machine learning systems require monitoring and evaluation.",
    "Retrieval augmented generation improves LLM accuracy.",
    "Vector databases enable semantic search."
]

embeddings = embedder.generate_embeddings(documents)

vector_index = VectorIndex(len(embeddings[0]))
vector_index.add_documents(embeddings, documents)

rag = RAGPipeline(vector_index)


class Query(BaseModel):
    question: str


@app.post("/ask")

def ask(query: Query):

    answer = rag.query(query.question)

    return {"response": answer}
