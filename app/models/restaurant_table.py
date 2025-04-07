from sqlalchemy import Column, String, SmallInteger, CheckConstraint
from sqlalchemy.orm import relationship

from app.utils.mixins import IdMixin, TimestampMixin
from metadata import Base


class RestaurantTable(IdMixin, TimestampMixin, Base):
    __tablename__ = "restaurant_table"
    __table_args__ = (
        CheckConstraint('seats > 0', name='check_seats_positive'),
    )

    name = Column(String(50), nullable=False, index=True, unique=True)
    seats = Column(SmallInteger, nullable=False, default=4)
    location = Column(String(100), nullable=True, index=True)

    reservations = relationship("Reservation", back_populates="restaurant_table", lazy='noload')
