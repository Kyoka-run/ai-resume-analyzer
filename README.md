# AI Resume Analyzer

An intelligent resume-job matching system powered by multi-agent AI workflow. The system analyzes resumes against job descriptions and provides detailed matching scores with actionable insights.

## Features

- **Resume Analysis**: Extracts key information (skills, experience, education) from PDF resumes
- **JD Analysis**: Parses job descriptions to identify requirements and qualifications
- **Smart Matching**: Compares resume against JD with detailed scoring (0-100)
- **Gap Analysis**: Identifies strengths and missing qualifications
- **Hiring Recommendation**: Provides actionable hiring suggestions

## Tech Stack

| Technology | Purpose |
|------------|---------|
| **LangChain** | LLM interaction and prompt management |
| **LangGraph** | Multi-agent workflow orchestration |
| **OpenAI GPT-4o-mini** | Large language model |
| **PyPDF** | PDF text extraction |
| **Python 3.10+** | Runtime environment |

## Architecture
```
┌─────────────────────────────────────────────────────────┐
│                    LangGraph Workflow                   │
│                                                         │
│   resume_agent ──────┐                                  │
│   (analyze resume)   ├───→ matcher_agent ───→ Result   │
│   jd_agent ──────────┘     (score & compare)            │
│   (analyze JD)                                          │
└─────────────────────────────────────────────────────────┘
```

### Agents

| Agent | Input | Output |
|-------|-------|--------|
| **Resume Agent** | Resume PDF | Structured resume data (name, skills, experience, education) |
| **JD Agent** | Job description text | Structured requirements (required skills, experience, education) |
| **Matcher Agent** | Resume + JD analysis | Match score, strengths, gaps, recommendation |

## Project Structure
```
ai-resume-analyzer/
├── main.py                 # Entry point
├── agents/
│   ├── resume_agent.py     # Resume parsing agent
│   ├── jd_agent.py         # JD parsing agent
│   └── matcher_agent.py    # Matching & scoring agent
├── graph/
│   ├── state.py            # State definition
│   └── workflow.py         # LangGraph workflow
├── utils/
│   └── pdf_loader.py       # PDF & text file utilities
└── data/
    ├── sample_resume.pdf   # Sample resume for testing
    └── sample_jd.txt       # Sample job description
```

## Getting Started

### Prerequisites

- Python 3.10 or higher
- OpenAI API key

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/ai-resume-analyzer.git
cd ai-resume-analyzer
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure environment variables
```bash
# Create .env file
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

### Usage

1. Place your resume PDF in `data/sample_resume.pdf`
2. Place job description in `data/sample_jd.txt`
3. Run the analyzer
```bash
python main.py
```

## License

MIT License