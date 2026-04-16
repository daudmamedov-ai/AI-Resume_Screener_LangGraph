# Промпт для извлечения данных
EXTRACT_PROMPT = """
You are an expert HR assistant. Extract structured information from the provided resume text.
Resume: {resume_text}
"""

# Промпт для оценки соответствия
ANALYZE_PROMPT = """
Compare the Candidate Profile with the Job Description.
Evaluate if the candidate is a good fit.

Candidate Profile: {profile}
Job Description: {job_desc}

Return a structured analysis.
"""