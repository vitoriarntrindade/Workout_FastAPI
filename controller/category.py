from typing import List
from uuid import uuid4

from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy import select

from models.category import CategoryModel
from schemas.category import CategoryIn, CategoryOut
from contrib.dependencies import DatabaseDependency

router = APIRouter()


@router.post(
    "/",
    summary="Criar nova categoria",
    status_code=status.HTTP_201_CREATED,
    response_model=CategoryOut
)
async def post(
        db_session: DatabaseDependency,
        category_in: CategoryIn = Body(...)
) -> CategoryOut:
    category_out = CategoryOut(id=uuid4(), **category_in.model_dump())
    category_model = CategoryModel(**category_out.model_dump())

    db_session.add(category_model)
    await db_session.commit()

    return category_out


@router.get(
    "/",
    summary="Consultar todas categorias",
    status_code=status.HTTP_200_OK,
    response_model=List[CategoryOut]
)
async def query(db_session: DatabaseDependency) -> List[CategoryOut]:
    categories: list[CategoryOut] = (await db_session.execute(select(CategoryModel))).scalars().all()
    return [CategoryOut.model_validate(category) for category in categories]


@router.get(
    "/{id}",
    summary="Consulta uma Categoria pelo ID",
    status_code=status.HTTP_200_OK,
    response_model=CategoryOut
)
async def query(id: UUID4, db_session: DatabaseDependency) -> CategoryOut:
    category: CategoryOut = (
        await db_session.execute(select(CategoryModel).filter_by(id=id))).scalars().one_or_none()

    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Categoria de ID {id} não foi encontrada')
    return category


