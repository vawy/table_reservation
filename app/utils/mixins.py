import datetime

from sqlalchemy import Column, DateTime, func, Integer


class IdMixin:
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )


class CreatedAtMixin:
    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.datetime.utcnow,
        server_default=func.now()
    )


class TimestampMixin(CreatedAtMixin):
    updated_at = Column(
        DateTime,
        nullable=False,
        server_default=func.now(),
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow
    )
