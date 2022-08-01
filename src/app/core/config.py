import pathlib

from pydantic import BaseSettings

from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str = 'UGC API'
    PROJECT_DESCRIPTION: str = 'API для записи пользовательского контента'
    API_VERSION = '0.1.0'

    quotes_json_file_path: pathlib.Path = pathlib.Path('../data/quotes.json.gz')


    class Config:  # noqa: WPS431
        env_file = ".env"


settings = Settings()
