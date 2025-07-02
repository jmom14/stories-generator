from api.services.base_service import BaseService
from api.errors import ServiceError
from api.config import settings
from google import genai


class GeminiService(BaseService):

    def __init__(self):
        self.model = settings.gemini_model
        self.client = genai.Client(api_key=settings.gemini_key)

    def submit_prompt(self, prompt) -> str:
        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
            )
            return response.text

        except Exception as e:
            error_message = str(e)
            raise ServiceError(f"Unexpected error: {error_message}") from e
