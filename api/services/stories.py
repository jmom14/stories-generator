from openai import OpenAI
import json
from config import settings
from helper import prompts
from writers.writerfactory import WriterFactory

ROLE = "user"
SIZES = {
    "small": "story of 200 words",
    "medium": "story of 300 words",
    "large": "story of 400 words",
}


def create_story(story):
    client = OpenAI(
        api_key=settings.openai_key,
    )

    prompt = prompts.get_story_prompt(
        story.words, story.language, "story of 1000 words"
    )
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": ROLE,
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo",
        )
        data = json.loads(chat_completion.choices[0].message.content)
        writer_factory = WriterFactory(story.format)
        writer = writer_factory.create_writer(data["title"], "ChatGPT", data["content"])
        book_file = writer.write()
        return book_file

    except Exception as e:
        print(f"error: {str(e)}")
        return ""
