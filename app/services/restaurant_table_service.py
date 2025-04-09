from sqlalchemy.orm import joinedload

from app.services.base import BaseService
from app.models import RestaurantTable


class RestaurantTableService(BaseService):
    list_options = []
    options = [
        *list_options,
        joinedload(RestaurantTable.reservations)
    ]

    def __init__(self, session, options=None):
        super().__init__(session=session, model=RestaurantTable, options=options)
