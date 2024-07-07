from uuid import uuid4
from typing import Annotated
from pydantic import Field
from fastapitest.contrib.schemas import BaseSchema

class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example="CT King", max_length=20)]
    endereco: Annotated[str, Field(description='Endereço do centro de treinamento', example="Rua X, 002", max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietário do centro de treinamento', example="Marcos", max_length=30)]

class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example="CT King", max_length=20)]
    
class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[uuid4, Field(description="Identificador do centro de treinamento")]