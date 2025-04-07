from fastapi import APIRouter, Request, status


router = APIRouter(
    tags=["reservations"],
    prefix="/reservations"
)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    summary="Список всех броней",
    description="Список всех броней"
)
async def get_all(
        request: Request
):
    pass


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    summary="Создать новую бронь",
    description="Создать новую бронь"
)
async def create_one(
        request: Request
):
    pass


@router.delete(
    "/{model_id}",
    status_code=status.HTTP_200_OK,
    summary="Удалить бронь",
    description="Удалить бронь"
)
async def delete_one(
        request: Request,
        model_id: int
):
    pass
