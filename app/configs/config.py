from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SECRET_KEY: str
    TOKEN_EXPIRE_IN_MINUTES: int
    ALGORITHM: str = "HS256"
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
