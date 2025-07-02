from typing import Literal
from enum import Enum
from api.services.gemini_service import GeminiService
from api.services.chatgpt_service import ChatGPTService
from api.services.claude_service import ClaudeService


class Service(Enum):
    GEMINI = "gemini"
    CLAUDE = "claude"
    CHATGPT = "chatgpt"


class ServiceFactory:

    @staticmethod
    def get_service(service_name: Literal["gemini", "claude", "chatgpt"]):
        if service_name == Service.GEMINI.value:
            return GeminiService()

        elif service_name == Service.CLAUDE.value:
            return ClaudeService()

        elif service_name == Service.CHATGPT.value:
            return ChatGPTService()

        else:
            raise ValueError(f"Unknown service: {service_name}")
