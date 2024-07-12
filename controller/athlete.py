from datetime import datetime
from typing import List
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
    category_name = athlete_in.category.name
    training_center_name = athlete_in.training_center.name

    category = (
        await db_session.execute(select(
            CategoryModel).filter_by(name=category_name))).scalars().one_or_none()

    if not category:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f'Categoria {category_name} não foi encontrada')

    training_center = (
        await db_session.execute(select(
            TrainingCenterModel
        ).filter_by(name=training_center_name))).scalars().one_or_none()

    if not training_center:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f'Centro de Treinamento {training_center_name} não foi encontrado')

    try:
        athlete_out = AthleteOut(id=uuid4(), created_at=datetime.utcnow(), **athlete_in.model_dump())
        athlete = AthleteModel(**athlete_out.model_dump(exclude={'category', 'training_center'}))

        athlete.category_id = category.pk_id
        athlete.training_center_id = training_center.pk_id

        db_session.add(athlete)
        await db_session.commit()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Ocorreu um erro ao inserir os dados no banco de dados.'
        )

    return athlete_out


@router.get(
    "/",
    summary="Consultar todos atletas",
    status_code=status.HTTP_200_OK,
    response_model=List[AthleteOut]
)
async def query(db_session: DatabaseDependency) -> List[AthleteOut]:
    athletes: list[AthleteOut] = (await db_session.execute(select(AthleteModel))).scalars().all()
    return athletes


@router.get(
    "/{id}",
    summary="Consulta um atleta pelo ID",
    status_code=status.HTTP_200_OK,
    response_model=AthleteOut
)
async def query(id: UUID4, db_session: DatabaseDependency) -> AthleteOut:
    athlete: AthleteOut = (
        await db_session.execute(select(AthleteModel).filter_by(id=id))).scalars().one_or_none()

    if not athlete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Atleta de ID {id} não foi encontrado')
    return athlete


@router.patch(
    '/id',
    summary="Edita um atleta pelo ID",
    status_code=status.HTTP_200_OK,
    response_model=AthleteOut
)
async def patch(
        id: UUID4,
        db_session: DatabaseDependency,
        atleta_up: AthleteUpdate = Body(...)
) -> AthleteOut:
    athlete = (
        await db_session.execute(select(AthleteModel).filter_by(id=id))).scalars().one_or_none()

    if not athlete:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Atleta de ID {id}'
        )

    athlete_update = atleta_up.model_dump(exclude_unset=True)

    for key, value in athlete_update.items():
        setattr(athlete, key, value)

    await db_session.commit()
    await db_session.refresh(athlete)

    return athlete


@router.delete(
    '/{id}',
    summary='Deletar um Atleta pelo id',
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete(id: UUID4, db_session: DatabaseDependency) -> None:
    athlete: AthleteOut = (
        await db_session.execute(select(AthleteModel).filter_by(id=id))
    ).scalars().first()

    if not athlete:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Atleta não encontrado no id: {id}'
        )

    await db_session.delete(athlete)
    await db_session.commit()