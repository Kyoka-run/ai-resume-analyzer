"""
Resume Job Matcher - Main Entry Point

A multi-agent AI system that analyzes resumes and matches them against job descriptions.

Tech Stack:
- LangChain: LLM interaction and prompt management
- LangGraph: Multi-agent workflow orchestration
- OpenAI GPT-4o-mini: Language model
- PyPDF: PDF text extraction
"""

import os
from dotenv import load_dotenv

from utils.pdf_loader import load_pdf, load_text_file
from graph.workflow import create_workflow


def main():
    """
    Main function to run the resume matching workflow.
    """
    # Load environment variables
    load_dotenv()

    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in .env file")
        return

    print("=" * 50)
    print("Resume Job Matcher")
    print("=" * 50)

    # Load input files
    try:
        print("\n[1/4] Loading resume...")
        resume_text = load_pdf("data/sample_resume.pdf")
        print(f"✓ Resume loaded ({len(resume_text)} characters)")

        print("\n[2/4] Loading job description...")
        jd_text = load_text_file("data/sample_jd.txt")
        print(f"✓ JD loaded ({len(jd_text)} characters)")

    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Please add sample_resume.pdf and sample_jd.txt to the data/ folder")
        return

    # Create workflow
    print("\n[3/4] Creating workflow...")
    app = create_workflow()
    print("✓ Workflow created")

    # Prepare initial state
    initial_state = {
        "resume_text": resume_text,
        "jd_text": jd_text,
        "resume_analysis": None,
        "jd_analysis": None,
        "match_result": None
    }

    # Run workflow
    print("\n[4/4] Running analysis...")
    print("-" * 50)

    # Stream results to see each agent's output
    for step in app.stream(initial_state):
        for node_name, output in step.items():
            print(f"\n>> {node_name} completed")

    # Get final result
    final_state = app.invoke(initial_state)

    print("\n" + "=" * 50)
    print("FINAL RESULT")
    print("=" * 50)
    print(final_state["match_result"])


if __name__ == "__main__":
    main()