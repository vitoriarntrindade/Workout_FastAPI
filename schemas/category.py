from typing import Annotated

from pydantic import UUID4, Field
from contrib.schemas import BaseSchema


class CategoryIn(BaseSchema):
    name: Annotated[str, Field(description='Nome da categoria', example='Scale', max_length=10)]


class CategoryOut(CategoryIn):
    id: Annotated[UUID4, Field(description='Identificador da categoria')]