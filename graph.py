import json
from datetime import datetime
from typing import Dict, Any
from langgraph.graph import StateGraph, END

# Импортируем модели, промпты и функции
from models import ScreenerState, CandidateProfile, FitAnalysis 
from prompts import EXTRACT_PROMPT, ANALYZE_PROMPT
from llm_functions import call_llm_structured

# --- Node 1: Загрузка данных ---
def n_ingest(state: ScreenerState):
    print("--- [Node 1]: Ingesting Data ---")
    return state

# --- Node 2: Извлечение профиля (1-й вызов ИИ) ---
def n_extract_profile(state: ScreenerState):
    print("--- [Node 2]: Extracting Profile ---")
    # Используем актуальную модель Gemini 3 через нашу функцию
    prompt = EXTRACT_PROMPT.format(resume_text=state.resume_text)
    profile = call_llm_structured(prompt, CandidateProfile)
    return {"candidate_profile": profile.model_dump()}

# --- Node 3: Анализ соответствия (2-й вызов ИИ) ---
def n_analyze_fit(state: ScreenerState):
    print("--- [Node 3]: Analyzing Fit ---")
    # Сравниваем профиль из state с описанием вакансии
    prompt = ANALYZE_PROMPT.format(
        profile=state.candidate_profile, 
        job_desc=state.job_description
    )
    analysis = call_llm_structured(prompt, FitAnalysis)
    return {"fit_analysis": analysis.model_dump()}

# --- Node 4: Сохранение отчета в JSON ---
def n_export(state: ScreenerState):
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"final_report_{timestamp}.json"
    
    report = {
        "candidate_info": state.candidate_profile,
        "job_analysis": state.fit_analysis,
        "processed_at": datetime.now().isoformat()
    }
    
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4, ensure_ascii=False)
    
    return {"final_report_path": file_name}

# --- Сборка графа ---
def build_graph():
    builder = StateGraph(ScreenerState)
    
    # Добавляем все 4 узла
    builder.add_node("ingest", n_ingest)
    builder.add_node("extract", n_extract_profile)
    builder.add_node("analyze", n_analyze_fit)
    builder.add_node("export", n_export)
    
    # Настраиваем связи
    builder.set_entry_point("ingest")
    builder.add_edge("ingest", "extract")
    builder.add_edge("extract", "analyze")
    builder.add_edge("analyze", "export")
    builder.add_edge("export", END)
    
    return builder.compile()