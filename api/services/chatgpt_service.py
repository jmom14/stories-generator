from api.services.base_service import BaseService
from api.errors import ServiceError
from openai import OpenAI, OpenAIError
from api.config import settings


class ChatGPTService(BaseService):

    ROLE = "user"

    def __init__(self):
        self.model = settings.openai_model
        self.client = OpenAI(api_key=settings.openai_key)
        super().__init__()

    def submit_prompt(self, prompt: str) -> str:
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[{"role": self.ROLE, "content": prompt}],
                model=self.model,
            )
            return chat_completion.choices[0].message.content

        except OpenAIError as e:
            error_message = str(e)
            raise OpenAIError(f"Error with OpenAI API: {error_message}") from e
        except Exception as e:
            error_message = str(e)
            raise ServiceError(f"Unexpected error: {error_message}") from e
