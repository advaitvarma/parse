# Parse

## Features

* **Resume and Job Description Input:**
  * File upload interface supporting standard document formats (PDF, DOCX) .
  * Plain text input field for pasting job requirements .
  * Parsing module to extract raw text and structured data from submitted documents .
* **Compatibility Scoring Engine:**
  * Text comparison between the parsed resume and the job description .
  * Score calculation based on frequency analysis, exact keyword intersection, and semantic similarity .
  * Output generated as a distinct percentage or numerical index .
* **Keyword Analysis and Skill Upgrade Roadmap:**
  * Extraction of requisite technical terms, required skills, and domain-specific vocabulary from the job description .
  * Cross-referencing against the resume to identify missing competencies and keywords .
  * Generation of a structured, step-by-step roadmap with actionable methods to acquire missing skills .
* **Company Recommendation Engine:**
  * Analysis of industry, role type, and required skills to query related market entities .
  * Output of alternative companies and similar job listings to improve application success probability based on the user's skillset .

---

## User Flow

1. **Submit Inputs:** Upload a resume file (PDF/DOCX) and paste the target job description text into the interface .
2. **Text Parsing:** Parse processes and extracts raw text and structured data from both inputs .
3. **Scoring & Evaluation:** The scoring engine evaluates the resume against the job description using frequency, keyword intersection, and semantic analysis to produce a compatibility score .
4. **Gap Analysis & Roadmap:** Parse identifies missing skills/keywords and delivers a step-by-step skill upgrade plan .
5. **Opportunity Recommendations:** The system queries related market entities to present alternative companies and similar job listings tailored to the candidate's profile .
