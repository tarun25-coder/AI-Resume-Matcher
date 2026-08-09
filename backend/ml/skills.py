import re


SKILLS = [
    "java",
    "python",
    "c",
    "c++",
    "c#",
    "javascript",
    "typescript",

    "html",
    "css",
    "react",
    "angular",
    "node.js",

    "spring",
    "spring boot",
    "django",
    "flask",
    "fastapi",

    "mysql",
    "postgresql",
    "mongodb",
    "sqlite",

    "git",
    "github",
    "docker",
    "kubernetes",
    "aws",
    "azure",

    "rest api",
    "graphql",

    "machine learning",
    "deep learning",
    "artificial intelligence",
    "natural language processing",

    "tensorflow",
    "pytorch",
    "scikit-learn",

    "pandas",
    "numpy",
    "opencv",

    "data structures",
    "algorithms",
    "sql",
]


def extract_skills(text: str) -> list[str]:
    """
    Extract known technical skills from text.

    Longer skills are matched first so that:
    'spring boot' does not also produce 'spring'.
    """

    if not text:
        return []

    text = text.lower()

    found_skills = []

    # Match longer/more specific skills first
    sorted_skills = sorted(
        SKILLS,
        key=len,
        reverse=True
    )

    for skill in sorted_skills:
        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

        if re.search(pattern, text):
            found_skills.append(skill)

            # Remove the matched skill from the text
            # so shorter overlapping skills aren't detected.
            text = re.sub(pattern, " ", text)

    return sorted(found_skills)


def compare_skills(
    resume_text: str,
    job_text: str
) -> dict:
    """
    Compare skills found in a resume and job description.
    """

    resume_skills = set(extract_skills(resume_text))
    job_skills = set(extract_skills(job_text))

    matched = resume_skills.intersection(job_skills)
    missing = job_skills - resume_skills

    return {
        "resume_skills": sorted(resume_skills),
        "job_skills": sorted(job_skills),
        "matched_skills": sorted(matched),
        "missing_skills": sorted(missing),
    }


def calculate_skill_match(resume_text: str, job_text: str) -> float:
    """
    Calculate the percentage of required job skills
    that are present in the resume.
    """

    resume_skills = set(extract_skills(resume_text))
    job_skills = set(extract_skills(job_text))

    if not job_skills:
        return 0.0

    matched_skills = resume_skills.intersection(job_skills)

    score = (len(matched_skills) / len(job_skills)) * 100

    return round(score, 2)