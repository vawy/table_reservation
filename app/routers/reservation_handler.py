from fastapi import APIRouter, Request, status
from fastapi_pagination import Page

from app.services.reservation_service import ReservationService
from app.schemas.reservation_schema import ReservationResponseSchema, ReservationCreateSchema
from app.schemas.base_responses import BasicResultResponseSchema


router = APIRouter(
    tags=["reservations"],
    prefix="/reservations"
)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    summary="Список всех броней",
    description="Список всех броней",
    response_model=Page[ReservationResponseSchema]
)
async def get_all(
        request: Request
):
    async with request.app.state.db.get_master_session() as session:
        reservation_service = ReservationService(session=session, options=ReservationService.options)
        return await reservation_service.get_all()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    summary="Создать новую бронь",
    description="Создать новую бронь",
    response_model=BasicResultResponseSchema
)
async def create_one(
        request: Request,
        body: ReservationCreateSchema
) -> BasicResultResponseSchema:
    async with request.app.state.db.get_master_session() as session:
        reservation_service = ReservationService(session=session)
        await reservation_service.create_one(body=body)
    return BasicResultResponseSchema()



@router.delete(
    "/{model_id}",
    status_code=status.HTTP_200_OK,
    summary="Удалить бронь",
    description="Удалить бронь",
    response_model=BasicResultResponseSchema
)
async def delete_one(
        request: Request,
        model_id: int
) -> BasicResultResponseSchema:
    async with request.app.state.db.get_master_session() as session:
        reservation_service = ReservationService(session=session)
        await reservation_service.delete_one(model_id=model_id)
    return BasicResultResponseSchema()
