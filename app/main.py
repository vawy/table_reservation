import os
import sys
import logging
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi_pagination import add_pagination

from app.utils.base import bind_routes, lifespan
from app.routers import routes
from app.settings import Settings, settings

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("app.log", encoding="utf-8")
    ]
)
logger = logging.getLogger(__name__)


async def log_requests(request: Request, call_next):
    logger.info(f"Request: {request.method} {request.url}")
    try:
        response = await call_next(request)
        logger.info(f"Response: {response.status_code}")
        return response
    except Exception as e:
        logger.error(f"Error: {str(e)}", exc_info=True)
        raise

def add_exception_handlers(fastapi_app: FastAPI):
    @fastapi_app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        logger.error(f"Unhandled exception: {exc}", exc_info=True)
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal Server Error"}
        )


def make_app(app_settings: Settings) -> FastAPI:
    logger.info("Creating FastAPI application")
    fastapi_app = FastAPI(
        title="Table reservation",
        lifespan=lifespan,
        docs_url="/api/table_reservation/swagger"
    )

    fastapi_app.middleware("http")(log_requests)
    logger.info("Binding routes")
    bind_routes(app=fastapi_app, routes=routes)
    add_pagination(fastapi_app)
    add_exception_handlers(fastapi_app=fastapi_app)

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
