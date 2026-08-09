def calculate_final_score(
    similarity_score: float,
    skill_score: float,
    keyword_score: float
) -> float:
    """
    Calculate the final resume-job match score.

    Weights:
    - 50% text similarity
    - 30% skill match
    - 20% keyword coverage
    """

    final_score = (
        similarity_score * 0.50
        + skill_score * 0.30
        + keyword_score * 0.20
    )

    return round(final_score, 2)

import re


def extract_keywords(text: str) -> set[str]:
    """
    Extract meaningful words from text.
    """

    if not text:
        return set()

    words = re.findall(r"\b[a-zA-Z][a-zA-Z+#.]*\b", text.lower())

    stop_words = {
        "the", "and", "or", "a", "an", "to", "of",
        "in", "for", "with", "on", "is", "are", "we",
        "our", "this", "that", "as", "be", "will",
        "you", "your", "from", "at", "by"
    }

    return {
        word
        for word in words
        if word not in stop_words and len(word) > 2
    }


def calculate_keyword_coverage(
    resume_text: str,
    job_text: str
) -> float:
    """
    Calculate how many job-description keywords
    appear in the resume.
    """

    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_text)

    if not job_keywords:
        return 0.0

    matched_keywords = resume_keywords.intersection(job_keywords)

    score = (
        len(matched_keywords) /
        len(job_keywords)
    ) * 100

    return round(score, 2)