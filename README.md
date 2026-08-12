# 🤖 AI Resume Matcher

An AI-powered web application that analyzes a candidate's resume against a job description and provides a **resume–job match score, skill analysis, keyword coverage, and missing skills**.

The project combines a **React + TypeScript frontend**, **FastAPI backend**, and a lightweight **machine-learning analysis pipeline** to help candidates understand how well their resume matches a particular job.

## 🌐 Live Demo

**Frontend:**
https://ai-resume-matcher-laixipxa0-tarun25-coders-projects.vercel.app

**Backend API:**
https://ai-resume-matcher-c1q2.onrender.com

**API Documentation:**
https://ai-resume-matcher-c1q2.onrender.com/docs

> The backend is hosted on Render's free tier, so the first request after a period of inactivity may take longer while the service starts.

---

## ✨ Features

### 📄 Resume Upload

* Upload resumes in PDF format.
* PDF file validation.
* Maximum file size of **5 MB**.
* Automatic text extraction from the uploaded resume.

### 📝 Job Description Analysis

* Paste any job description into the application.
* The system analyzes the job requirements against the uploaded resume.

### 🧠 Machine Learning Analysis

The application uses text-based machine-learning techniques to calculate similarity between the resume and job description.

Current analysis includes:

* TF-IDF-based text similarity
* Skill matching
* Keyword coverage
* Combined final match score

### 🛠️ Skill Matching

The application identifies:

* Skills found in the resume
* Skills required by the job
* Matched skills
* Missing skills

Example:

```text
Matched Skills:
Java
Git
MySQL

Missing Skills:
Spring Boot
Docker
AWS
```

### 📊 Match Report

The application provides:

* Overall Match Score
* Text Similarity Score
* Skill Match Percentage
* Keyword Coverage
* Matched Skills
* Missing Skills

### 🔐 Input Validation & Error Handling

The backend includes:

* PDF-only validation
* 5 MB file-size restriction
* Empty job-description validation
* Controlled HTTP errors
* Unexpected error handling
* CORS configuration

---

## 🏗️ System Architecture

```text
                    User
                      │
                      ▼
              React Frontend
              Vercel Hosting
                      │
                      │ HTTPS
                      ▼
              FastAPI Backend
              Render Hosting
                      │
              ┌───────┴────────┐
              ▼                ▼
        PDF Text Parser    Job Description
              │                │
              └───────┬────────┘
                      ▼
               ML Analysis
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       TF-IDF      Skill       Keyword
      Similarity   Matching     Analysis
          │           │           │
          └───────────┼───────────┘
                      ▼
                Final Score
                      │
                      ▼
              Analysis Report
                      │
                      ▼
                React UI
```

---

## 🛠️ Technology Stack

### Frontend

* React
* TypeScript
* Vite
* CSS
* JavaScript/TypeScript Fetch API

### Backend

* Python
* FastAPI
* Uvicorn
* Pydantic
* Python Multipart

### Machine Learning & Data Processing

* Scikit-learn
* NumPy
* Pandas
* Joblib
* SciPy

### PDF Processing

* pypdf

### Development & Deployment

* Git
* GitHub
* VS Code
* Vercel — Frontend
* Render — Backend

---

## 📁 Project Structure

```text
AI-Resume-Matcher/
│
├── backend/
│   ├── __init__.py
│   ├── main.py
│   ├── Procfile
│   ├── requirements.txt
│   │
│   ├── ml/
│   │   ├── __init__.py
│   │   ├── analyzer.py
│   │   ├── pdf_parser.py
│   │   ├── preprocessing.py
│   │   ├── scoring.py
│   │   └── skills.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── resume_analyzer.py
│   │
│   └── test_data/
│       └── resume.pdf
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.tsx
│   │   ├── App.css
│   │   └── ...
│   ├── .env.example
│   ├── package.json
│   ├── tsconfig.json
│   └── vite.config.ts
│
├── .gitignore
└── README.md
```

---

## ⚙️ How the Application Works

### Step 1 — Upload Resume

The user uploads a PDF resume.

The backend validates:

```text
File exists
     ↓
PDF format?
     ↓
Size ≤ 5 MB?
```

### Step 2 — Extract Resume Text

The PDF parser extracts readable text from the uploaded document.

### Step 3 — Enter Job Description

The user provides the target job description.

### Step 4 — Analyze Text Similarity

The system compares the resume and job description using TF-IDF-based text similarity.

### Step 5 — Compare Skills

Relevant skills are extracted from both the resume and job description.

The system determines:

```text
Resume Skills
      +
Job Skills
      ↓
Matched Skills
Missing Skills
```

### Step 6 — Calculate Keyword Coverage

The system checks how much of the relevant job-related terminology is represented in the resume.

### Step 7 — Calculate Final Score

The analysis combines the available scoring components into an overall match score.

### Step 8 — Display Results

The frontend displays the analysis in a user-friendly format.

---

## 🚀 Run Locally

### Prerequisites

Make sure you have:

* Python
* Node.js
* npm
* Git

### 1. Clone the repository

```bash
git clone https://github.com/tarun25-coder/AI-Resume-Matcher.git
cd AI-Resume-Matcher
```

### 2. Create Python virtual environment

```bash
python -m venv venv
```

Activate it on Windows Git Bash:

```bash
source venv/Scripts/activate
```

### 3. Install backend dependencies

```bash
pip install -r backend/requirements.txt
```

### 4. Start the backend

From the project root:

```bash
python -m uvicorn backend.main:app --reload
```

The backend will be available at:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

Health check:

```text
http://127.0.0.1:8000/health
```

Expected response:

```json
{
  "status": "healthy"
}
```

---

## 💻 Run the Frontend

Open another terminal.

```bash
cd frontend
npm install
```

Create:

```text
frontend/.env
```

with:

```env
VITE_API_URL=http://127.0.0.1:8000
```

Then start the development server:

```bash
npm run dev
```

Open:

```text
http://localhost:5173
```

---

## 🔑 Environment Variables

### Frontend

The frontend uses:

```env
VITE_API_URL=http://127.0.0.1:8000
```

For production, this points to the deployed backend:

```env
VITE_API_URL=https://ai-resume-matcher-c1q2.onrender.com
```

The actual `.env` file should **not** be committed to GitHub.

Use `.env.example` as the safe configuration template.

---

## 🔌 API Endpoints

### Health Check

```http
GET /health
```

Response:

```json
{
  "status": "healthy"
}
```

### Resume Analysis

```http
POST /analyze
```

Parameters:

```text
resume            PDF file
job_description   Job description text
```

Example response:

```json
{
  "match_score": 31.2,
  "similarity_score": 9.3,
  "skill_match": 63.6,
  "keyword_coverage": 37.0,
  "resume_skills": [
    "java",
    "python",
    "git",
    "github",
    "mysql"
  ],
  "job_skills": [
    "java",
    "spring boot",
    "mysql",
    "docker"
  ],
  "matched_skills": [
    "java",
    "mysql",
    "git"
  ],
  "missing_skills": [
    "spring boot",
    "docker"
  ]
}
```

---

## 🧪 Testing

The application has been tested with multiple job descriptions to verify that the analysis changes according to the supplied job requirements.

Example test categories:

* Java Backend Developer
* Data Analyst
* Machine Learning Engineer

The same resume produces different match results for different job descriptions, demonstrating that the analysis depends on the relationship between the resume and target job.

---

## 🔒 Security & Validation

The application currently implements:

* PDF file validation
* 5 MB upload limit
* Empty input validation
* Controlled API error responses
* CORS restrictions
* `.env` protection through `.gitignore`
* Python virtual environment exclusion
* Node.js dependency exclusion

---

## ☁️ Deployment

### Backend

The FastAPI backend is deployed on **Render**.

Configuration:

```text
Root Directory:
.

Build Command:
pip install -r backend/requirements.txt

Start Command:
uvicorn backend.main:app --host 0.0.0.0 --port $PORT
```

### Frontend

The React frontend is deployed on **Vercel**.

Configuration:

```text
Root Directory:
frontend

Build Command:
npm run build

Output Directory:
dist
```

The production frontend uses:

```text
VITE_API_URL
```

to communicate with the deployed FastAPI backend.

---

## 🚧 Future Improvements

The current version is a functional MVP. Planned improvements include:

* Resume improvement recommendations
* Better skill-gap analysis
* More advanced semantic similarity
* Improved scoring methodology
* Visual score charts
* Resume section analysis
* Job-specific keyword recommendations
* Improved skill extraction
* Support for additional resume formats
* More robust NLP/LLM-based analysis
* Better handling of synonyms and related technologies

---

## 🎯 Project Goal

The goal of AI Resume Matcher is to help students and job seekers understand:

> **"How well does my resume match this particular job?"**

Instead of manually comparing a resume with every job description, the application provides an automated analysis and highlights areas that may need improvement.

---

## 👨‍💻 Author

**Tarun S**

Information Science & Engineering
JNNCE, Shivamogga, Karnataka

### Profiles

* GitHub: https://github.com/tarun25-coder
* LinkedIn: https://www.linkedin.com/in/tarun-s-eng

---

## 📜 License

This project is intended for educational, portfolio, and learning purposes.
