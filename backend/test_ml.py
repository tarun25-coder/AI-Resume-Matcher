from backend.ml.analyzer import calculate_similarity
from backend.ml.skills import (
    compare_skills,
    calculate_skill_match
)
from backend.ml.scoring import (
    calculate_keyword_coverage,
    calculate_final_score
)


resume = """
Software Engineer with experience in Java, Python, MySQL,
Spring Boot, Git and REST API development.
"""

job_description = """
We are looking for a Software Engineer with strong Java,
Spring Boot, MySQL, REST API, Git and Docker skills.
"""


# ---------------------------------------
# 1. TF-IDF similarity
# ---------------------------------------

similarity_score = calculate_similarity(
    resume,
    job_description
)

print(f"Resume-Job Similarity: {similarity_score}%")


# ---------------------------------------
# 2. Skill analysis
# ---------------------------------------

skill_result = compare_skills(
    resume,
    job_description
)

print("\nResume Skills:")
print(skill_result["resume_skills"])

print("\nJob Required Skills:")
print(skill_result["job_skills"])

print("\nMatched Skills:")
print(skill_result["matched_skills"])

print("\nMissing Skills:")
print(skill_result["missing_skills"])


# ---------------------------------------
# 3. Skill match score
# ---------------------------------------

skill_score = calculate_skill_match(
    resume,
    job_description
)

print(f"\nSkill Match Score: {skill_score}%")


# ---------------------------------------
# 4. Keyword coverage
# ---------------------------------------

keyword_score = calculate_keyword_coverage(
    resume,
    job_description
)

print(f"Keyword Coverage: {keyword_score}%")


# ---------------------------------------
# 5. Final score
# ---------------------------------------

final_score = calculate_final_score(
    similarity_score,
    skill_score,
    keyword_score
)

print(f"\nFINAL MATCH SCORE: {final_score}%")