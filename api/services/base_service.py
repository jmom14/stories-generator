from abc import ABC, abstractmethod


class BaseService(ABC):

    @abstractmethod
    def submit_prompt(self, prompt: str) -> str:
        pass
