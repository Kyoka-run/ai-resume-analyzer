"""
LangGraph workflow definition.
Orchestrates the multi-agent resume matching pipeline.
"""

from langgraph.graph import StateGraph, END

from graph.state import ResumeMatcherState
from agents.resume_agent import analyze_resume
from agents.jd_agent import analyze_jd
from agents.matcher_agent import match_resume_to_jd


def create_workflow():
    """
    Create and compile the LangGraph workflow.

    Workflow:
        resume_agent ──┐
                       ├──→ matcher_agent ──→ END
        jd_agent ──────┘

    Returns:
        Compiled LangGraph application
    """
    # Initialize the graph with our state schema
    workflow = StateGraph(ResumeMatcherState)

    # Add nodes (agents)
    workflow.add_node("resume_agent", analyze_resume)
    workflow.add_node("jd_agent", analyze_jd)
    workflow.add_node("matcher_agent", match_resume_to_jd)

    # Set entry point - both resume and jd agents start in parallel
    workflow.set_entry_point("resume_agent")

    # Define edges (execution order)
    # resume_agent and jd_agent run first, then matcher_agent combines results
    workflow.add_edge("resume_agent", "jd_agent")
    workflow.add_edge("jd_agent", "matcher_agent")
    workflow.add_edge("matcher_agent", END)

    # Compile the workflow
    app = workflow.compile()

    return app