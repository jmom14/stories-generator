from api.services.base_service import BaseService
from api.config import settings
import anthropic


class ClaudeService(BaseService):

    ROLE = "user"

    def __init__(self):
        self.model = settings.cloude_model
        self.client = anthropic.Anthropic(api_key=settings.cloude_key)

    def submit_prompt(self, prompt) -> str:
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=1024,
                messages=[{"role": self.ROLE, "content": prompt}],
            )
            return response.content

        except Exception as e:
            error_message = str(e)
            raise Exception(f"Unexpected error: {error_message}") from e
