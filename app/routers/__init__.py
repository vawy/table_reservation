from app.routers.reservation_handler import router as reservation_router
from app.routers.restaurant_table_handler import router as restaurant_table_router

routes = [
    reservation_router,
    restaurant_table_router
]

__all__ = [
    "routes",
]