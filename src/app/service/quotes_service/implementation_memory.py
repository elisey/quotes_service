import gzip
import json
import pathlib

from .interface import QuotesServiceInterface, Quote, QuoteNotFound


class QuotesServiceMemory(QuotesServiceInterface):
    def __init__(self, data_path: pathlib.Path):
        self.data = self.__load_data(data_path)

    def __load_data(self, data_path: pathlib.Path) -> dict:
        print('load data from memory')
        with gzip.open(data_path) as json_file:
            return json.load(json_file)

    async def get_by_id(self, item_id: int) -> Quote:
        try:
            text = self.data[str(item_id)]
        except KeyError:
            raise QuoteNotFound
        return Quote(
            item_id=item_id,
            text=text
        )

    async def get_by_range(self, start_id: int, size: int) -> list[Quote]:
        raise NotImplemented
