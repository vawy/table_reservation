from datetime import datetime, timezone

from pydantic import BaseModel, Field
from app.utils.fields_constraints import NameField


class BasicReservationSchema(BaseModel):
    customer_name: NameField
    reservation_time: datetime = Field(gt=datetime.now(tz=timezone.utc))
    restaurant_table_id: int
    duration_minutes: int = Field(gt=0)


class ReservationCreateSchema(BasicReservationSchema):
    pass


class ReservationResponseSchema(BasicReservationSchema):
    id: int
    reservation_end_time: datetime
