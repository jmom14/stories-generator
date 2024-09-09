from openai import OpenAI, OpenAIError
import json
from config import settings
from helper import prompts
from writers.writerfactory import WriterFactory
import logging


ROLE = "user"
STORY_SIZES = {
    "small": "that contains around 500 words",
    "medium": "that contains around 1000 words",
    "large": "that contains around 2000 words",
}


def generate_chat_completion(client, prompt):
    return client.chat.completions.create(
        messages=[{"role": ROLE, "content": prompt}],
        model=settings.openai_model or "gpt-3.5-turbo",
    )


def create_story(story):
    client = OpenAI(api_key=settings.openai_key)
    prompt = prompts.get_story_prompt(story.words, story.language, STORY_SIZES["large"])
    try:
        chat_completion = generate_chat_completion(client, prompt)
        content = chat_completion.choices[0].message.content
        data = json.loads(content)
        writer_factory = WriterFactory(story.format)
        writer = writer_factory.create_writer(data["title"], "ChatGPT", data["content"])
        book, filename = writer.write()
        return book, filename

    except json.JSONDecodeError as e:
        print(content)
        logging.error(f"Error parsing JSON: {str(e)}")
    except OpenAIError as e:
        logging.error(f"Error with OpenAI API: {str(e)}")
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")

    return "", ""
