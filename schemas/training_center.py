from typing import Annotated

from pydantic import Field, UUID4
from contrib.schemas import BaseSchema


class TrainingCenterIn(BaseSchema):
    name: Annotated[str, Field(description='Nome do centro de treinamento', example='CT Monster', max_length=20)]
    address: Annotated[str, Field(description='Endereço do centro de treinamento', example='Rua Belém, 230', max_length=60)]
    owner: Annotated[str, Field(description='Proprietário do centro de treinamento', example='Guilherme', max_length=30)]


class TrainingCenter(BaseSchema):
    name: Annotated[str, Field(description='Nome do centro de treinamento', example='CT Amazonas', max_length=20)]


class TrainingCenterOut(TrainingCenterIn):
    id: Annotated[UUID4, Field(description='Identificador do centro de treinamento')]
