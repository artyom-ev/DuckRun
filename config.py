from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    LOCAL_DB_USERNAME: str
    LOCAL_DB_PASSWORD: str
    LOCAL_DB_HOST: str
    LOCAL_DB_PORT: int
    LOCAL_DB_NAME: str

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

    @property
    def DATABASE_URL_LOCAL_psycopg(self):
        return (
            "postgresql+psycopg://" +
            f"{self.LOCAL_DB_USERNAME}:{self.LOCAL_DB_PASSWORD}" +
            f"@{self.LOCAL_DB_HOST}:{self.LOCAL_DB_PORT}/{self.LOCAL_DB_NAME}"
        )

    @property
    def DATABASE_URL_LOCAL_asyncpg(self):
        return (
            "postgresql+asyncpg://" +
            f"{self.LOCAL_DB_USERNAME}:{self.LOCAL_DB_PASSWORD}" +
            f"@{self.LOCAL_DB_HOST}:{self.LOCAL_DB_PORT}/{self.LOCAL_DB_NAME}"
        )

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()