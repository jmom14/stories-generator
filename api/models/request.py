from pydantic import BaseModel
from typing import List


class StoryRequest(BaseModel):
    language: str = "english"
    words: List[str]
    format: str = "epub"
