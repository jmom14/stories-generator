import json
import logging
from openai import OpenAIError
from api.helper import prompts, utils
from api.writers.writer_factory import WriterFactory
from api.services.service_factory import ServiceFactory


ROLE = "user"
STORY_SIZES = {
    "small": "that contains around 500 words",
    "medium": "that contains around 1000 words",
    "large": "that contains around 2000 words",
}


def create_story(story):
    prompt = prompts.get_story_prompt(story.words, story.language, STORY_SIZES["small"])
    try:
        service = ServiceFactory.get_service("gemini")
        content = service.submit_prompt(prompt)

        clean_content = utils.extract_markdown_content(content)
        data = json.loads(clean_content)

        writer = WriterFactory.get_writer(
            story.format, data["title"], "ChatGPT", data["content"]
        )
        book, filename = writer.write()
        return book, filename

    except json.JSONDecodeError as e:
        error_message = str(e)
        logging.error("Error parsing JSON: %s", error_message)

    except OpenAIError as e:
        error_message = str(e)
        logging.error("Error with OpenAI API: %s", error_message)

    return None
