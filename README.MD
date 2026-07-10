# ResearchRoots

## Overview
ResearchRoots is a beginner-first research guidance platform that helps students move from curiosity to active participation in research.

Many students are interested in research but don't know where to begin. Existing resources are scattered across multiple websites, making the journey confusing. ResearchRoots aims to provide one structured path from learning the basics to discovering opportunities and building a research profile.

## Current Features
- User Registration
- User Login
- Password Hashing
- Session Authentication
- Protected Dashboard
- Logout
- SQLite Database Integration

## Planned Features
- Research onboarding questionnaire
- Personalized roadmap generation
- Progress tracking
- Streak system
- Competitions and opportunity discovery
- Collaboration with researchers, institutions and think tanks

## Tech Stack
- HTML
- CSS
- JavaScript
- Python
- Flask
- SQLite
- SQLAlchemy

## Project Structure
```text
app.py
models.py
templates/
static/
researchroots.db
```

## Running the Project
1. Create a virtual environment.
2. Install dependencies.
3. Configure `.env` with `SECRET_KEY`.
4. Run:

```bash
python app.py
```

The application starts locally and creates the SQLite database automatically if it does not already exist.
