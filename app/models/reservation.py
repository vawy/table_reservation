from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Index, CheckConstraint, SmallInteger
from sqlalchemy.orm import relationship

from app.utils.mixins import IdMixin, TimestampMixin
from metadata import Base


class Reservation(IdMixin, TimestampMixin, Base):
    __tablename__ = "reservation"
    __table_args__ = (
        Index('idx_reservation_table_time', 'restaurant_table_id', 'reservation_time'),
        CheckConstraint('duration_minutes > 0', name='check_duration_positive'),
        CheckConstraint('reservation_time >= CURRENT_TIMESTAMP', name='check_future_reservation'),
    )

    customer_name = Column(String(100), nullable=False, index=True)
    restaurant_table_id = Column(Integer, ForeignKey('restaurant_table.id', ondelete="CASCADE"), nullable=False)
    reservation_time = Column(DateTime, nullable=False, index=True)
    duration_minutes = Column(SmallInteger, nullable=False)

    restaurant_table = relationship("RestaurantTable", back_populates="reservations", lazy='noload')
