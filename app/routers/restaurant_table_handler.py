from fastapi import APIRouter, Request, status

from app.services.restaurant_table_service import RestaurantTableService

router = APIRouter(
    tags=["tables"],
    prefix="/tables"
)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    summary="Список всех столиков",
    description="Список всех столиков"
)
async def get_all(
        request: Request
):
    async with request.app.state.db.get_master_session() as session:
        restaurant_table_service = RestaurantTableService(session=session, options=RestaurantTableService.list_options)
        return await restaurant_table_service.get_all()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    summary="Создать новый столик",
    description="Создать новый столик"
)
async def create_one(
        request: Request
):
    pass


@router.delete(
    "/{model_id}",
    status_code=status.HTTP_200_OK,
    summary="Удалить столик",
    description="Удалить столик"
)
async def delete_one(
        request: Request,
        model_id: int
):
    async with request.app.state.db.get_master_session() as session:
        restaurant_table_service = RestaurantTableService(session=session)
        return await restaurant_table_service.delete_one(model_id=model_id)
