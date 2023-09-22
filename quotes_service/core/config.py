import pathlib

from dotenv import load_dotenv
from pydantic_settings import BaseSettings


load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str = "Quote API"
    PROJECT_DESCRIPTION: str = "API for getting funny quotes"
    API_VERSION: str = "0.1.0"

    quotes_json_file_path: pathlib.Path = pathlib.Path("../data/quotes.json.gz")

    class ConfigDict:
        env_file = ".env"


settings = Settings()
