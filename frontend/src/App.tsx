import { useState } from "react";
import "./App.css";

interface AnalysisResult {
  match_score: number;
  similarity_score: number;
  skill_match: number;
  keyword_coverage: number;
  resume_skills: string[];
  job_skills: string[];
  matched_skills: string[];
  missing_skills: string[];
}

function App() {
  const [resume, setResume] = useState<File | null>(null);
  const [jobDescription, setJobDescription] = useState("");
  const [result, setResult] = useState<AnalysisResult | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  // Handle resume PDF selection
  const handleFileChange = (
  event: React.ChangeEvent<HTMLInputElement>
) => {
  const file = event.target.files?.[0];

  if (!file) {
    return;
  }

  // Check file type
  if (file.type !== "application/pdf") {
    setError("Please upload a PDF file.");
    setResume(null);
    setResult(null);
    return;
  }

  // Check file size - maximum 5 MB
  const MAX_FILE_SIZE = 5 * 1024 * 1024;

  if (file.size > MAX_FILE_SIZE) {
    setError(
      "Resume file is too large. Maximum size is 5 MB."
    );
    setResume(null);
    setResult(null);
    return;
  }

  // File is valid
  setResume(file);
  setError("");
  setResult(null);
};

  // Send resume and job description to FastAPI
  const analyzeResume = async () => {
    if (!resume) {
      setError("Please upload your resume PDF.");
      return;
    }

    if (!jobDescription.trim()) {
      setError("Please enter a job description.");
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);

    const formData = new FormData();

    formData.append("resume", resume);
    formData.append("job_description", jobDescription);

try {
  const response = await fetch(
    `${import.meta.env.VITE_API_URL}/analyze`,
    {
      method: "POST",
      body: formData,
    }
  );

  const data = await response.json();

  if (!response.ok) {
    throw new Error(
      data.detail || "Failed to analyze resume."
    );
  }

  setResult(data);
} catch (err) {
      setError(
        err instanceof Error
          ? err.message
          : "Something went wrong while analyzing the resume."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">

      {/* Header */}
      <header className="header">
        <div className="logo">
          AI Resume Matcher
        </div>

        <p>
          Analyze your resume against any job description
        </p>
      </header>


      <main className="container">

        {/* Hero */}
        <section className="hero">
          <h1>
            Find out how well your resume matches a job.
          </h1>

          <p>
            Upload your resume and paste the job description.
            Our ML engine will analyze your skills and provide
            a detailed match report.
          </p>
        </section>


        {/* Resume Upload */}
        <section className="card">

          <h2>1. Upload your resume</h2>

          <label className="upload-box">

            <input
              type="file"
              accept=".pdf"
              onChange={handleFileChange}
            />

            <div className="upload-content">

              <div className="upload-icon">
                📄
              </div>

              <strong>
                {resume
                  ? resume.name
                  : "Choose your resume PDF"}
              </strong>

              <span>
                PDF files only
              </span>

            </div>

          </label>

        </section>


        {/* Job Description */}
        <section className="card">

          <h2>2. Job description</h2>

          <textarea
            value={jobDescription}
            onChange={(event) => {
              setJobDescription(event.target.value);
              setResult(null);
            }}
            placeholder="Paste the job description here..."
          />

          <div className="character-count">
            {jobDescription.length} characters
          </div>

        </section>


        {/* Error Message */}
        {error && (
          <div className="error-message">
            {error}
          </div>
        )}


        {/* Analyze Button */}
        <button
          className="analyze-button"
          disabled={
            !resume ||
            !jobDescription.trim() ||
            loading
          }
          onClick={analyzeResume}
        >
          {loading
            ? "Analyzing Resume..."
            : "Analyze Resume"}
        </button>


        {/* Results */}
        {result && (
          <section className="results">

            <div className="result-header">

              <h2>
                Your Match Score
              </h2>

              <div className="score">
                {result.match_score.toFixed(1)}%
              </div>

            </div>


            {/* Score Cards */}
            <div className="score-grid">

              <div className="score-card">
                <span>
                  Text Similarity
                </span>

                <strong>
                  {result.similarity_score.toFixed(1)}%
                </strong>
              </div>


              <div className="score-card">
                <span>
                  Skill Match
                </span>

                <strong>
                  {result.skill_match.toFixed(1)}%
                </strong>
              </div>


              <div className="score-card">
                <span>
                  Keyword Coverage
                </span>

                <strong>
                  {result.keyword_coverage.toFixed(1)}%
                </strong>
              </div>

            </div>


            {/* Skills */}
            <div className="skills-section">

              {/* Matched Skills */}
              <div className="skill-group">

                <h3>
                  ✓ Matched Skills
                </h3>

                <div className="skill-list">

                  {result.matched_skills.length > 0 ? (
                    result.matched_skills.map((skill) => (
                      <span
                        className="skill matched"
                        key={skill}
                      >
                        {skill}
                      </span>
                    ))
                  ) : (
                    <p>
                      No matching skills found.
                    </p>
                  )}

                </div>

              </div>


              {/* Missing Skills */}
              <div className="skill-group">

                <h3>
                  ✗ Missing Skills
                </h3>

                <div className="skill-list">

                  {result.missing_skills.length > 0 ? (
                    result.missing_skills.map((skill) => (
                      <span
                        className="skill missing"
                        key={skill}
                      >
                        {skill}
                      </span>
                    ))
                  ) : (
                    <p>
                      No missing skills detected.
                    </p>
                  )}

                </div>

              </div>

            </div>

          </section>
        )}

      </main>


      {/* Footer */}
      <footer>
        <p>
          AI Resume Matcher • React + FastAPI + Machine Learning
        </p>
      </footer>

    </div>
  );
}

export default App;