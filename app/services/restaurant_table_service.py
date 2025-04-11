from typing import Optional

from fastapi import HTTPException
from fastapi_pagination import Params

from starlette import status

from sqlalchemy.orm import selectinload
from sqlalchemy.exc import IntegrityError

from app.services.base import BaseService
from app.models import RestaurantTable
from app.schemas.restaurant_table_schema import RestaurantTableCreateSchema


class RestaurantTableService(BaseService):
    list_options = [
        selectinload(RestaurantTable.reservations)
    ]
    options = [
        *list_options
    ]

    def __init__(self, session, options=None):
        super().__init__(session=session, model=RestaurantTable, options=options)


    async def create_one(self, body: RestaurantTableCreateSchema):
        model = RestaurantTable(
            name=body.name,
            seats=body.seats,
            location=body.location
        )

        try:
            self.session.add(model)
            await self.session.flush()
        except IntegrityError as err:
            await self.session.rollback()
            if "unique constraint" in str(err).lower():
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Table with name = '{body.name}' already exist!"
                )

            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="An error occurred while creating the table"
            )
