from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from backend.ml.preprocessing import clean_text


def calculate_similarity(resume_text: str, job_text: str) -> float:
    """
    Calculate similarity between a resume and job description
    using TF-IDF and cosine similarity.
    """

    resume_text = clean_text(resume_text)
    job_text = clean_text(job_text)

    if not resume_text or not job_text:
        return 0.0

    documents = [resume_text, job_text]

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2)
    )

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )[0][0]

    return round(similarity * 100, 2)