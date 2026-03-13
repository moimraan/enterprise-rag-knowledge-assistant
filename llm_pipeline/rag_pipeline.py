from embeddings.embedding_generator import EmbeddingGenerator

class RAGPipeline:

    def __init__(self, vector_index):
        self.embedder = EmbeddingGenerator()
        self.vector_index = vector_index

    def query(self, question):

        query_embedding = self.embedder.generate_embeddings([question])

        docs = self.vector_index.search(query_embedding)

        context = " ".join(docs)

        response = f"""
        Context:
        {context}

        Question:
        {question}

        Answer:
        """

        return response
