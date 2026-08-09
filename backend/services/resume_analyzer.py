import os
import tempfile

from backend.ml.pdf_parser import extract_text_from_pdf
from backend.ml.analyzer import calculate_similarity
from backend.ml.skills import compare_skills, calculate_skill_match
from backend.ml.scoring import (
    calculate_keyword_coverage,
    calculate_final_score,
)


def analyze_resume(
    pdf_bytes: bytes,
    job_description: str,
) -> dict:
    """
    Analyze a resume PDF against a job description.

    Returns similarity, skill, keyword, and final match scores
    along with matched and missing skills.
    """

    temp_path = None

    try:
        # Create a temporary PDF file
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as temp_file:
            temp_file.write(pdf_bytes)
            temp_path = temp_file.name

        # Extract text from the resume
        resume_text = extract_text_from_pdf(temp_path)

        if not resume_text:
            raise ValueError(
                "Could not extract text from the PDF."
            )

        # Calculate TF-IDF similarity
        similarity_score = calculate_similarity(
            resume_text,
            job_description
        )

        # Compare technical skills
        skill_result = compare_skills(
            resume_text,
            job_description
        )

        # Calculate skill match
        skill_score = calculate_skill_match(
            resume_text,
            job_description
        )

        # Calculate keyword coverage
        keyword_score = calculate_keyword_coverage(
            resume_text,
            job_description
        )

        # Calculate final score
        final_score = calculate_final_score(
            similarity_score,
            skill_score,
            keyword_score
        )

        return {
            "match_score": final_score,
            "similarity_score": similarity_score,
            "skill_match": skill_score,
            "keyword_coverage": keyword_score,
            "resume_skills": skill_result["resume_skills"],
            "job_skills": skill_result["job_skills"],
            "matched_skills": skill_result["matched_skills"],
            "missing_skills": skill_result["missing_skills"],
        }

    finally:
        # Delete the temporary PDF
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)