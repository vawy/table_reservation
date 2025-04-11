import os
import sys
import logging
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import uvicorn
from fastapi import FastAPI
from fastapi_pagination import add_pagination

from app.utils.base import bind_routes, lifespan
from app.routers import routes
from app.settings import Settings, settings

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def make_app(app_settings: Settings) -> FastAPI:
    logger.info("Creating FastAPI application")
    fastapi_app = FastAPI(
        title="Table reservation",
        lifespan=lifespan,
        docs_url="/api/table_reservation/swagger"
    )

    logger.info("Binding routes")
    bind_routes(app=fastapi_app, routes=routes)
    # add_pagination(fastapi_app)

    return fastapi_app


if __name__ == "__main__":
    try:
        logger.info("Starting application...")
        app = make_app(app_settings=settings)

        uvicorn_config = {
            "host": "0.0.0.0",
            "port": 8000,
            "log_config": None
        }
        uvicorn.run(app=app, **uvicorn_config)
    except Exception as e:
        logger.critical(f"Application failed to start: {e}")
        raise
