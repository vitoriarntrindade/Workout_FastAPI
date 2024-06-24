from datetime import datetime
from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from schemas.athlete import AthleteIn, AthleteOut, AthleteUpdate
from models.athlete import AthleteModel

from models.category import CategoryModel
from models.training_center import TrainingCenterModel

from contrib.dependencies import DatabaseDependency
from sqlalchemy.future import select

router = APIRouter()


@router.post(
    '/',
    summary='Criar novo atleta',
    status_code=status.HTTP_201_CREATED,
    response_model=AthleteOut
)
async def post(
    db_session: DatabaseDependency,
    athlete_in: AthleteIn = Body(...)
):
    pass