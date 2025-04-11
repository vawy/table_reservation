from pydantic import BaseModel, Field

from app.schemas.reservation_schema import ReservationResponseSchema
from app.utils.fields_constraints import NameField, LocationField


class BasicRestaurantTableSchema(BaseModel):
    name: NameField
    seats: int = Field(gt=0)
    location: LocationField | None


class RestaurantTableCreateSchema(BasicRestaurantTableSchema):
    pass


class SimpleRestaurantTableResponseSchema(BasicRestaurantTableSchema):
    id: int | None


class RestaurantTableResponseSchema(BasicRestaurantTableSchema):
    id: int | None
    reservations: list[ReservationResponseSchema]
