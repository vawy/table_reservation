from fastapi import APIRouter, Request, status

from app.services.reservation_service import ReservationService


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
    async with request.app.state.db.get_master_session() as session:
        reservation_service = ReservationService(session=session, options=ReservationService.list_options)
        return await reservation_service.get_all()


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
    async with request.app.state.db.get_master_session() as session:
        reservation_service = ReservationService(session=session)
        return await reservation_service.delete_one(model_id=model_id)
