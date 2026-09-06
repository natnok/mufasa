from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = "mufasa"
    app_version: str = "v3.02v"

    app_host: str = "0.0.0.0"
    app_port: int = 8000
    app_reload: bool = True


settings = Settings()
