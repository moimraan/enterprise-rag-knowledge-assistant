import faiss
import numpy as np

class VectorIndex:

    def __init__(self, dimension):
        self.index = faiss.IndexFlatL2(dimension)
        self.documents = []

    def add_documents(self, embeddings, docs):
        self.index.add(np.array(embeddings))
        self.documents.extend(docs)

    def search(self, query_embedding, k=3):
        distances, indices = self.index.search(query_embedding, k)

        results = []
        for idx in indices[0]:
            results.append(self.documents[idx])

        return results
