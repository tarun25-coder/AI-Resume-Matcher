from fastapi import FastAPI, File, Form, UploadFile, HTTPException

from backend.ml.pdf_parser import extract_text_from_pdf
from backend.ml.analyzer import calculate_similarity
from backend.ml.skills import compare_skills, calculate_skill_match
from backend.ml.scoring import (
    calculate_keyword_coverage,
    calculate_final_score,
)


app = FastAPI(
    title="AI Resume Matcher API",
    description="API for analyzing resumes against job descriptions.",
    version="1.0.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/analyze")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...),
):
    """
    Analyze a resume against a job description.
    """

    if not resume.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF resumes are supported."
        )

    # Read uploaded PDF
    pdf_bytes = await resume.read()

    # Save temporarily
    temp_path = "backend/temp_resume.pdf"

    with open(temp_path, "wb") as file:
        file.write(pdf_bytes)

    try:
        # Extract resume text
        resume_text = extract_text_from_pdf(temp_path)

        if not resume_text:
            raise HTTPException(
                status_code=400,
                detail="Could not extract text from the PDF."
            )

        # Calculate TF-IDF similarity
        similarity_score = calculate_similarity(
            resume_text,
            job_description
        )

        # Extract and compare skills
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
        # Remove temporary file
        import os

        if os.path.exists(temp_path):
            os.remove(temp_path)