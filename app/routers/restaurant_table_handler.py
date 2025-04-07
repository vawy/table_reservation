from fastapi import APIRouter, Request, status


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
    pass


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
    pass
