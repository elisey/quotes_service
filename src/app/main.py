import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1 import quotes
from core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.API_VERSION,
    docs_url='/api/v1/openapi',
    openapi_url='/api/v1/openapi.json',
    default_response_class=ORJSONResponse,
)


@app.on_event('startup')
async def startup_event():
    pass


@app.on_event('shutdown')
async def shutdown_event():
    pass


app.include_router(quotes.router, prefix='/api/v1/quotes', tags=['quotes'])

if __name__ == '__main__':
    uvicorn.run(
        'main:app'
    )
