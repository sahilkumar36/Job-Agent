# Job-Agent: AI-Powered Career Assistant

Job-Agent is a standout portfolio piece built with **Django**, **LangChain**, and **Google Gemini AI**. It allows users to upload job descriptions and receive an instant, AI-driven analysis of how well their skills match the role!


## Features
- **Premium Dashboard:** A modern, glassmorphism-inspired UI built with Vanilla CSS.
- **AI Resume Parsing:** Upload your PDF resume; Gemini automatically extracts your skills and profile.
- **AI Match Scoring:** Intelligent scoring (0-100%) based on semantic analysis of job requirements vs. your profile.
- **Skill Gap Analysis:** Automatically identifies matching and missing skills with red/green highlights.
- **AI Career Advice:** Actionable advice on how to bridge the gap for each specific job.
- **Agentic Logic:** Uses LangChain and Gemini 1.5 Flash to reason like a technical recruiter.

## Tech Stack
- **Backend:** Django 5.2
- **AI:** Google Gemini 1.5 Flash (via LangChain)
- **Frontend:** HTML5 / Vanilla CSS (Modern Aesthetics)
- **Environment:** Python 3.11+

## Setup
1. Clone the repository.
2. Create a `.env` file with your `GOOGLE_API_KEY`.
3. Run `pip install -r requirements.txt`.
4. Run `python manage.py migrate`.
5. Run `python manage.py runserver`.

---
Built by [Your Name] as part of an advanced AI Agent portfolio.
