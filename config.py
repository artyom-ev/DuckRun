from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str


    @property
    def DATABASE_URL_psycopg(self):
        return (
            "postgresql+psycopg://" +
            f"{self.DB_USERNAME}:{self.DB_PASSWORD}" +
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    @property
    def DATABASE_URL_asyncpg(self):
        return (
            "postgresql+asyncpg://" +
            f"{self.DB_USERNAME}:{self.DB_PASSWORD}" +
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()