"""
State definition for LangGraph workflow.
Defines the data structure passed between agents.
"""

from typing import TypedDict, Optional


class ResumeMatcherState(TypedDict):
    """
    State object that flows through the LangGraph workflow.
    Each agent reads from and writes to this state.
    """

    # Input data
    resume_text: str  # Raw text extracted from resume PDF
    jd_text: str  # Job description text

    # Agent outputs
    resume_analysis: Optional[str]  # Parsed resume info (skills, experience, etc.)
    jd_analysis: Optional[str]  # Parsed JD requirements
    match_result: Optional[str]  # Final matching result and score