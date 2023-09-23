import typing
from functools import lru_cache
from http import HTTPStatus

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from starlette.responses import JSONResponse

from app.core.config import settings
from app.service.quotes.implementation_memory import QuotesServiceMemory
from app.service.quotes.interface import QuoteNotFound, QuotesServiceInterface


router = APIRouter()


class QuoteResponse(BaseModel):
    item_id: int
    text: str


@lru_cache
def get_quotes_service() -> QuotesServiceInterface:
    return QuotesServiceMemory(settings.quotes_json_file_path)


@router.get(
    "/{quote_id}",
    summary="Get quote by id",
    response_model=QuoteResponse,
)
async def get_quote(
    quote_id: int,
    quotes_service: QuotesServiceInterface = Depends(get_quotes_service),
) -> typing.Union[QuoteResponse, JSONResponse]:
    try:
        quote = await quotes_service.get_by_id(quote_id)
    except QuoteNotFound:
        return JSONResponse(status_code=HTTPStatus.NOT_FOUND, content={"message": "Item not found"})
    return QuoteResponse(item_id=quote.item_id, text=quote.text)
