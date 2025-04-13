from datetime import timedelta, datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Index, SmallInteger, select
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.sql.expression import text

from app.utils.mixins import IdMixin, TimestampMixin
from metadata import Base


class Reservation(IdMixin, TimestampMixin, Base):
    __tablename__ = "reservation"
    __table_args__ = (
        Index('idx_reservation_table_time', 'restaurant_table_id', 'reservation_time'),
    )

    customer_name = Column(String(100), nullable=False, index=True)
    restaurant_table_id = Column(Integer, ForeignKey('restaurant_table.id', ondelete="CASCADE"), nullable=False)
    reservation_time = Column(DateTime(timezone=True), nullable=False, index=True)
    duration_minutes = Column(SmallInteger, nullable=False)

    restaurant_table = relationship("RestaurantTable", back_populates="reservations", lazy='noload')

    @hybrid_property
    def reservation_end_time(self):
        return self.reservation_time + timedelta(minutes=int(self.duration_minutes))

    @reservation_end_time.expression
    def reservation_end_time(cls):
        return cls.reservation_time + (cls.duration_minutes * text("INTERVAL '1 minute'"))

    @classmethod
    async def is_table_available(
            cls,
            session: AsyncSession,
            restaurant_table_id: int,
            start_time: datetime,
            end_time: datetime
    ) -> bool:
        existing = await session.scalar(
            select(cls)
            .where(
                cls.restaurant_table_id == restaurant_table_id,
                cls.reservation_time < end_time,
                cls.reservation_end_time > start_time
            )
        )
        return existing is None
