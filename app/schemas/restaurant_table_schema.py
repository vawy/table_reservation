from pydantic import BaseModel, Field


class BasicRestaurantTableSchema(BaseModel):
    name: str
    seats: int = Field(gt=0)
    location: str | None


class RestaurantTableCreateSchema(BasicRestaurantTableSchema):
    pass


class RestaurantTableResponseSchema(BasicRestaurantTableSchema):
    id: int | None
    reservations: list
