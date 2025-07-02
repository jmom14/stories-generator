from typing import List


def get_story_prompt(words: List[str], language: str, size: str) -> str:
    words = ", ".join(words)
    prompt = (
        f"Act as an exceptional fiction writer. Write an original {size} story in {language} of"
        + f"approximately 500 words that creatively incorporates the words '{words}' at"
        + "least once. Give the story an engaging title."
        + "Return the story as a valid JSON object with two attributes:"
        + "'title': a string containing the title of the story"
        + "'content': a string containing the full story"
        + "The final output should be:"
        + "Wrapped in double quotes so it can be used as a JSON string"
        + "Escaped properly using json.dumps() in Python, so all keys and string values"
        + " use double quotes Safe to deserialize using json.loads()"
        + "If using special characters like curly quotes (’), either escape them using"
        + "Unicode (e.g., \u2019) or ensure the string is UTF-8 encoded"
    )
    return prompt
