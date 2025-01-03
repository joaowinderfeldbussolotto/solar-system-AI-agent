from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    MISTRAL_AI_KEY = os.getenv("MISTRAL_AI_KEY")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

settings = Settings()