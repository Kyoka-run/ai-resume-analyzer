"""
Resume Analysis Agent.
Extracts structured information from resume text.
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


# Define prompt template
RESUME_ANALYSIS_PROMPT = ChatPromptTemplate.from_messages([
    ("system", """You are a professional HR assistant specialized in resume analysis.
Your task is to extract and summarize key information from the resume.

Extract the following:
1. **Name**: Candidate's full name
2. **Contact**: Email, phone, location
3. **Skills**: Technical and soft skills listed
4. **Experience**: Job titles, companies, years of experience
5. **Education**: Degrees, institutions, graduation years
6. **Projects**: Notable projects if any

Be concise and structured in your response."""),

    ("human", "Please analyze this resume:\n\n{resume_text}")
])


def analyze_resume(state: dict) -> dict:
    """
    Agent function that analyzes resume text.
    """
    # Initialize LLM inside function (after .env is loaded)
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    chain = RESUME_ANALYSIS_PROMPT | llm

    resume_text = state["resume_text"]
    response = chain.invoke({"resume_text": resume_text})

    return {"resume_analysis": response.content}