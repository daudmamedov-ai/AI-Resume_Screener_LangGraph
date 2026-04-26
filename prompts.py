EXTRACT_PROMPT = """
You are an expert HR Data Scientist. Your task is to parse the following resume and extract key professional entities.
Focus on identifying technical stack, years of experience, and educational background.

Resume Content:
{resume_text}

Instructions:
1. Normalize skill names (e.g., 'Py' -> 'Python').
2. Calculate total years of experience as a float.
3. If information is missing, use "Not specified".
"""

ANALYZE_PROMPT = """
You are a Senior Technical Recruiter. Compare the Candidate Profile against the Job Description.

Candidate Profile: 
{profile}

Job Description: 
{job_desc}

Evaluation Criteria:
1. Technical Match: Does the candidate have the required stack?
2. Experience Level: Does the seniority match the requirements?
3. Gap Analysis: Identify exactly which critical skills are missing.

Provide a cold, objective score from 0-100 and a final hiring recommendation.
"""