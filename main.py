import os
from graph import build_graph
from models import ScreenerState

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def main():
    # Проверяем файлы
    resume_path = "data/resume.txt"
    job_path = "data/job.txt"
    
    if not os.path.exists(resume_path) or not os.path.exists(job_path):
        print("Error: Please create resume.txt and job.txt in data/ folder")
        return

    # Загружаем данные
    initial_state = ScreenerState(
        resume_text=read_file(resume_path),
        job_description=read_file(job_path)
    )

    # Запускаем систему
    app = build_graph()
    final_state = app.invoke(initial_state)

    # Вывод результата
    print("\n" + "="*50)
    print("FINAL CANDIDATE PROFILE:")
    print(final_state["candidate_profile"])
    print("\nFIT ANALYSIS:")
    print(final_state["fit_analysis"])
    print("="*50)
    # Печатаем путь к файлу, который вернул нам узел export
    print(f"DONE! Full report saved to: {final_state.get('final_report_path')}")
    print("="*50)

if __name__ == "__main__":
    main()