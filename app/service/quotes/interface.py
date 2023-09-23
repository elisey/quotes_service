import dataclasses
from abc import ABC, abstractmethod


class QuoteNotFound(Exception):
    """Quote not found exception."""


@dataclasses.dataclass
class Quote:
    item_id: int
    text: str


class QuotesServiceInterface(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    async def get_by_id(self, item_id: int) -> Quote:
        pass

    @abstractmethod
    async def get_by_range(self, start_id: int, size: int) -> list[Quote]:
        pass
