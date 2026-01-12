"""
Job Description Analysis Agent.
Extracts requirements and qualifications from JD.
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


JD_ANALYSIS_PROMPT = ChatPromptTemplate.from_messages([
    ("system", """You are a professional HR assistant specialized in job description analysis.
Your task is to extract key requirements from the job description.

Extract the following:
1. **Job Title**: The position name
2. **Required Skills**: Must-have technical skills
3. **Preferred Skills**: Nice-to-have skills
4. **Experience Required**: Years and type of experience needed
5. **Education Required**: Degree requirements
6. **Key Responsibilities**: Main job duties

Be concise and structured in your response."""),

    ("human", "Please analyze this job description:\n\n{jd_text}")
])


def analyze_jd(state: dict) -> dict:
    """
    Agent function that analyzes job description.
    """
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    chain = JD_ANALYSIS_PROMPT | llm

    jd_text = state["jd_text"]
    response = chain.invoke({"jd_text": jd_text})

    return {"jd_analysis": response.content}