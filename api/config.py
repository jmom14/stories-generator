from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Stories API"

    openai_key: str | None = None
    openai_model: str = "gpt-3.5-turbo"

    gemini_key: str | None = None
    gemini_model: str = "gemini-2.5-flash"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
