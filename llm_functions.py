import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langsmith import traceable

load_dotenv()

# Инициализация модели
llm = ChatGoogleGenerativeAI(
    model="gemini-flash-latest", # Убираем -latest, пробуем чистый вариант
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0,
    # Добавляем параметр, который иногда лечит 404 на старых эндпоинтах
    convert_system_message_to_human=True 
)
@traceable(name="llm_structured_output")
def call_llm_structured(prompt: str, output_model):
    # Метод .with_structured_output заставляет ИИ вернуть данные строго по нашей Pydantic модели
    structured_llm = llm.with_structured_output(output_model)
    return structured_llm.invoke(prompt)