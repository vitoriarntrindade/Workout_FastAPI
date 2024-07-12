from typing import List
from uuid import uuid4

from fastapi import APIRouter, Body, status
from sqlalchemy import select
from schemas.training_center import TrainingCenterOut, TrainingCenterIn
from models.training_center import TrainingCenterModel
from contrib.dependencies import DatabaseDependency


router = APIRouter()


@router.post(
    "/",
    summary="Criar um novo centro de treinamento",
    status_code=status.HTTP_201_CREATED,
    response_model=TrainingCenterOut
)
async def post(
    db_session: DatabaseDependency,
    training_center_in: TrainingCenterIn = Body(...)
):
    training_center_out = TrainingCenterOut(id=uuid4(), **training_center_in.model_dump())
    training_center = TrainingCenterModel(**training_center_out.model_dump())

    db_session.add(training_center)
    await db_session.commit()

    return training_center

@router.get(
    '/',
    summary="Retorna uma lista com todos centros de treinamento",
    status_code=status.HTTP_200_OK,
    response_model=TrainingCenterOut
)
async def query(db_session: DatabaseDependency) -> List[TrainingCenterOut]:
    training_centers: List[TrainingCenterOut] = (await db_session.execute(select(TrainingCenterModel))).scalars().all()

    return training_centers

