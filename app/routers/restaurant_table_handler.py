from fastapi import APIRouter, Request, status
from fastapi_pagination import Page

from app.services.restaurant_table_service import RestaurantTableService
from app.schemas.base_responses import BasicResultResponseSchema
from app.schemas.restaurant_table_schema import RestaurantTableResponseSchema, RestaurantTableCreateSchema


router = APIRouter(
    tags=["tables"],
    prefix="/tables"
)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    summary="Список всех столиков",
    description="Список всех столиков",
    response_model=Page[RestaurantTableResponseSchema]
)
async def get_all(
        request: Request
):
    async with request.app.state.db.get_master_session() as session:
        restaurant_table_service = RestaurantTableService(session=session, options=RestaurantTableService.options)
        return await restaurant_table_service.get_all()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    summary="Создать новый столик",
    description="Создать новый столик",
    response_model=BasicResultResponseSchema
)
async def create_one(
        request: Request,
        body: RestaurantTableCreateSchema
) -> BasicResultResponseSchema:
    async with request.app.state.db.get_master_session() as session:
        restaurant_table_service = RestaurantTableService(session=session)
        await restaurant_table_service.create_one(body=body)
    return BasicResultResponseSchema()


@router.delete(
    "/{model_id}",
    status_code=status.HTTP_200_OK,
    summary="Удалить столик",
    description="Удалить столик",
    response_model=BasicResultResponseSchema
)
async def delete_one(
        request: Request,
        model_id: int
) -> BasicResultResponseSchema:
    async with request.app.state.db.get_master_session() as session:
        restaurant_table_service = RestaurantTableService(session=session)
        await restaurant_table_service.delete_one(model_id=model_id)
    return BasicResultResponseSchema()
