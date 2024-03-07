from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def retrieve_documents(query, documents):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents + [query])
    similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    ranked_documents_indices = similarity_scores.argsort()[0][::-1]
    return ranked_documents_indices
if __name__ == "__main__":
    documents = [
        "This is the first document.",
        "This document is the second document.",
        "And this is the third one.",
        "Is this the first document?",
    ]
    query = "This is the second document."
    ranked_documents_indices = retrieve_documents(query, documents)
    print("Ranked Documents:")
    for idx in ranked_documents_indices:
        print(f"Document {idx + 1}: {documents[idx]}")
