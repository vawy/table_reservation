from typing import Type, Optional

from fastapi import HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from fastapi_pagination import Params

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.strategy_options import LoaderOption
from sqlalchemy.exc import IntegrityError

from starlette import status

from metadata import Base


class BaseService:
    def __init__(self, session: AsyncSession, model: Type[Base], options: list[LoaderOption] | None = None):
        self.session = session
        self.model = model
        self.options = options or []


    async def get_all(self):
        query = select(self.model)

        if self.options:
            query = query.options(*self.options)

        result = (await self.session.scalars(query)).all()

        return result


    async def get_one(self, model_id: int):
        query = select(self.model).where(self.model.id == model_id)

        if self.options:
            query = query.options(*self.options)

        model = await self.session.scalar(query)

        if not model:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Model {self.model.__name__} with ID={model_id} was not found",
            )

        return model


    async def delete_one(self, model_id: int):
        model = await self.get_one(model_id=model_id)

        await self.session.delete(model)

        try:
            await self.session.flush()
        except IntegrityError as err:
            await self.session.rollback()
            raise err
