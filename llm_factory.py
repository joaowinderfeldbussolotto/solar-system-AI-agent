
from typing import Optional
from langchain_mistralai import ChatMistralAI
from langchain_groq import ChatGroq
from config import settings

class LLMFactory:
    @staticmethod
    def create(
        provider: str,
        model: Optional[str] = None,
        temperature: float = 0,
        max_retries: int = 4
    ):
        provider = provider.lower()
        
        if provider == "mistral":
            return ChatMistralAI(
                model=model or "open-mixtral-8x7b",
                temperature=temperature,
                max_retries=max_retries,
                api_key=settings.MISTRAL_AI_KEY
            )
        
        elif provider == "groq":
            return ChatGroq(
                model=model or "llama-3.1-70b-versatile",
                temperature=temperature,
                max_retries=max_retries,
                api_key=settings.GROQ_API_KEY
            )
        
        else:
            raise ValueError(f"Provider {provider} not supported. Use 'mistral' or 'groq'")