"""
Resume-JD Matcher Agent.
Compares resume against job requirements and provides matching score.
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


MATCHER_PROMPT = ChatPromptTemplate.from_messages([
    ("system", """You are a professional recruitment AI assistant.
Your task is to evaluate how well a candidate's resume matches a job description.

**Scoring Criteria (Total: 100 points)**:
- Skills Match: 35 points
- Experience Match: 35 points  
- Education Match: 15 points
- Overall Fit: 15 points

**Instructions**:
1. Compare the resume analysis against the JD requirements
2. Score each category based on alignment
3. Identify strengths and gaps
4. Provide a final recommendation

**Output Format**:
## Match Score: [X]/100

### Score Breakdown:
- Skills: [X]/35
- Experience: [X]/35
- Education: [X]/15
- Overall Fit: [X]/15

### Strengths:
- [List key matching points]

### Gaps:
- [List missing requirements]

### Recommendation:
[Your hiring recommendation with reasoning]"""),

    ("human", """Please evaluate this candidate:

**Resume Analysis:**
{resume_analysis}

**Job Requirements:**
{jd_analysis}""")
])


def match_resume_to_jd(state: dict) -> dict:
    """
    Agent function that matches resume against job description.
    """
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    chain = MATCHER_PROMPT | llm

    response = chain.invoke({
        "resume_analysis": state["resume_analysis"],
        "jd_analysis": state["jd_analysis"]
    })

    return {"match_result": response.content}