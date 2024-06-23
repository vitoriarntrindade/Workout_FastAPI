from typing import Annotated, Optional
from pydantic import Field, PositiveFloat
from schemas.category import CategoryIn
from schemas.training_center import TrainingCenter
from contrib.schemas import BaseSchema, OutMixin


class Athlete(BaseSchema):
    name: Annotated[str, Field(description='Nome do atleta', example='Vitória', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', example="12345678910", max_length=11)]
    age: Annotated[int, Field(description='Idade do atleta', example=25)]
    weight: Annotated[PositiveFloat, Field(description='Peso do atleta', example=80.5)]
    height: Annotated[PositiveFloat, Field(description='Altura do atleta', example=1.65)]
    sex: Annotated[str, Field(description='Sexo do atleta', example='M', max_length=1)]
    category: Annotated[CategoryIn, Field(description='Categoria do atleta')]
    training_center: Annotated[TrainingCenter, Field(description='Centro de treinamento do atleta')]


class AthleteIn(Athlete):
    pass


class AthleteOut(Athlete, OutMixin):
    pass


class AthleteUpdate(BaseSchema):
    name: Annotated[Optional[str], Field(None, description='Nome do atleta', example='Joao', max_length=50)]
    age: Annotated[Optional[int], Field(None, description='Idade do atleta', example=25)]
