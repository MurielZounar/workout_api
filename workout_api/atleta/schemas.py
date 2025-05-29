from pydantic import Field, PositiveFloat, ConfigDict, BaseModel
from typing import Annotated, Optional

from workout_api.contrib.schemas import BaseSchema, OutMixin
from workout_api.categorias.schemas import CategoriaIn
from workout_api.centro_treinamento.schemas import CentroTreinamentoAtleta

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', examples=['João'], max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', examples=['12345678912'], max_length=11)]
    idade: Annotated[int, Field(description='Idade do atleta', examples=[25])] #examples vai dar erro por ser lista
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', examples=[75.5])]
    altura: Annotated[PositiveFloat, Field(description='Peso do atleta', examples=[1.70])]
    sexo: Annotated[str, Field(description='Sexo do atleta', examples=['M'], max_length=1)]
    categoria: Annotated[CategoriaIn, Field(description='Sexo do atleta')]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description='Centro de treinamento do atleta')]

class AtletaIn(Atleta):
    pass

class AtletaOut(Atleta, OutMixin):
    pass

class AtletaPublic(BaseModel):
    nome: Annotated[str, Field(description='Nome do atleta', examples=['João'], max_length=50)]
    categoria: Annotated[CategoriaIn, Field(description='Sexo do atleta')]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description='Centro de treinamento do atleta')]
    model_config = ConfigDict(from_attributes=True)

class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(None, description='Nome do atleta', examples=['João'], max_length=50)]
    idade: Annotated[Optional[int], Field(None, description='Idade do atleta', examples=[25])] #examples vai dar erro por ser lista
