import pytest

from service.quotes_service.implementation_memory import QuotesServiceMemory
from service.quotes_service.interface import QuoteNotFound


@pytest.fixture
def service(test_quotes_dir):
    service = QuotesServiceMemory(test_quotes_dir)
    yield service


@pytest.mark.parametrize(
    "item_id,expected_text",
    [
        (1, 'Это тестовая цитата'),
        (2, 'More test quote'),
        (4, 'Третьей цитаты нет'),
    ]
)
async def test_get_item_by_id(service, item_id, expected_text):
    quote = await service.get_by_id(item_id)
    assert quote.item_id == item_id
    assert quote.text == expected_text


@pytest.mark.parametrize(
    "item_id",
    [
        3,
        -1,
        100,
    ]
)
async def test_get_not_existing_item(service, item_id):
    with pytest.raises(QuoteNotFound):
        _ = await service.get_by_id(item_id)
