from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Stories API"
    openai_key: str
    openai_model: str = "gpt-3.5-turbo"
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
