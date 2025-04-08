import logging
import uvicorn
from fastapi import FastAPI

from app.utils.base import bind_routes, bind_events
from app.routers import routes
from app.settings import application_settings, Settings


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)


def make_app(app_settings: Settings) -> FastAPI:
    logger.info("Creating FastAPI application")
    fastapi_app = FastAPI(
        title="Table reservation",
        description="",
        docs_url="/api/table_reservation/swagger"
    )

    logger.info(f"Binding database with URL: {app_settings.database_url[:15]}...")
    bind_events(app=fastapi_app, db_url=app_settings.database_url)

    logger.info("Binding routes")
    bind_routes(app=fastapi_app, routes=routes)

    return fastapi_app

app = make_app(app_settings=application_settings)

if __name__ == "__main__":
    uvicorn.run(app="app.main:app", host="0.0.0.0", port=8000, reload=True)
