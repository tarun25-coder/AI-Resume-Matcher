from fastapi import (
    FastAPI,
    File,
    Form,
    UploadFile,
    HTTPException,
)

from backend.services.resume_analyzer import analyze_resume


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
async def analyze_resume_endpoint(
    resume: UploadFile = File(...),
    job_description: str = Form(...),
):
    """
    Analyze a resume against a job description.
    """

    if not resume.filename:
        raise HTTPException(
            status_code=400,
            detail="Resume file is required."
        )

    if not resume.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF resumes are supported."
        )

    if not job_description.strip():
        raise HTTPException(
            status_code=400,
            detail="Job description is required."
        )

    try:
        pdf_bytes = await resume.read()

        result = analyze_resume(
            pdf_bytes,
            job_description
        )

        return result

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )