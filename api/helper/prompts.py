from typing import List


def get_story_prompt(words: List[str], language: str, size: str) -> str:
    words = ", ".join(words)
    prompt = (
        f"Act as a Writer and Editorial and create a story {size} in {language} using the "
        + f"following words: {words} "
        + "give a title and return it in json format with title and content as attributes."
        + "For example:  { "
        + ' "title": "The Story of Tomorrow" '
        + ' "content ":'
        + '"When I think back to my love of storytelling and why I pursued a degree in journalism, '
        + "it comes back to these tall tales. The Story of Tomorrow is only"
        + "one of the countless real-life stories that I heard growing up. My family immigrated to"
        + "the United States from Iran sporadically beginning in 1977 following the revolution,"
        + "and there was no shortage of memories to share."
        + '"'
        + "}"
    )
    return prompt
