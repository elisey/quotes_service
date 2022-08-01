import pytest


@pytest.mark.parametrize(
    "item_id,expected_text",
    [
        (1, 'Это тестовая цитата'),
        (2, 'More test quote'),
        (4, 'Третьей цитаты нет'),
    ]
)
def test_get_item(test_client, item_id, expected_text):
    response = test_client.get(f'/api/v1/quotes/{item_id}')
    assert response.status_code == 200

    expected_data = {
        'item_id': item_id,
        'text': expected_text
    }

    assert response.json() == expected_data


@pytest.mark.parametrize(
    "item_id",
    [
        3,
        -1,
        100,
    ]
)
async def test_get_not_existing_item(test_client, item_id):
    response = test_client.get(f'/api/v1/quotes/{item_id}')
    assert response.status_code == 404
