from sqlalchemy.orm import joinedload

from app.services.base import BaseService
from app.models import Reservation


class ReservationService(BaseService):
    list_options = [
        joinedload(Reservation.restaurant_table)
    ]
    options = [
        *list_options
    ]

    def __init__(self, session, options=None):
        super().__init__(session=session, model=Reservation, options=options)
