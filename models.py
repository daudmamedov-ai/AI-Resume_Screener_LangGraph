from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field

# Модель профиля кандидата (после 1-го вызова LLM)
class CandidateProfile(BaseModel):
    full_name: str = Field(description="Full name of the candidate")
    skills: List[str] = Field(description="List of technical and soft skills")
    education: str = Field(description="Highest degree and university")
    experience_years: float = Field(description="Total years of work experience")
    current_role: str = Field(description="Current or most recent job title")

# Модель анализа соответствия (после 2-го вызова LLM)
class FitAnalysis(BaseModel):
    fit_score: int = Field(description="Score from 0 to 100")
    matched_skills: List[str] = Field(description="Skills that match the job description")
    missing_skills: List[str] = Field(description="Required skills that are missing in resume")
    recommendation: str = Field(description="Invite, Maybe, or Reject")
    reasoning: str = Field(description="Short explanation of the score")

# Состояние системы (State)
class ScreenerState(BaseModel):
    resume_text: str = ""
    job_description: str = ""
    candidate_profile: Optional[Dict[str, Any]] = None
    fit_analysis: Optional[Dict[str, Any]] = None
    final_report_path: str = ""