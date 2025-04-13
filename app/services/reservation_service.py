from datetime import timedelta, datetime, timezone

from fastapi import HTTPException

from starlette import status

from sqlalchemy import select, exists
from sqlalchemy.orm import joinedload
from sqlalchemy.exc import IntegrityError

from app.services.base import BaseService
from app.models import Reservation, RestaurantTable
from app.schemas.reservation_schema import ReservationCreateSchema


class ReservationService(BaseService):
    options = [
        joinedload(Reservation.restaurant_table)
    ]

    def __init__(self, session, options=None):
        super().__init__(session=session, model=Reservation, options=options)


    async def create_one(self, body: ReservationCreateSchema):
        table_exists = await self.session.scalar(
            select(RestaurantTable.id).where(RestaurantTable.id == body.restaurant_table_id)
        )

        if not table_exists:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Table with ID {body.restaurant_table_id} not found"
            )

        end_time = body.reservation_time + timedelta(minutes=body.duration_minutes)

        if not await Reservation.is_table_available(
                session=self.session,
                restaurant_table_id=body.restaurant_table_id,
                start_time=body.reservation_time,
                end_time=end_time
        ):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"The table with ID {body.restaurant_table_id} is already occupied at this time."
            )

        model = Reservation(**body.model_dump())

        try:
            self.session.add(model)
            await self.session.flush()
        except IntegrityError as err:
            await self.session.rollback()
            raise err
