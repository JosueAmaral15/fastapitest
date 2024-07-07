from datetime import datetime, timezone
from uuid import uuid4
from fastapi import APIRouter, status, Body, HTTPException
from fastapitest.atleta.schemas import AtletaIn, AtletaOut
from fastapitest.contrib.dependencies import DatabaseDependency
from fastapitest.atleta.models import AtletaModel
from fastapitest.categorias.models import CategoriaModel
from sqlalchemy.future import select
from fastapitest.centro_treinamento.models import CentroTreinamentoModel

router = APIRouter()

@router.post(
    '/', 
    summary='Criar um novo atleta',
    status_code=status.HTTP_201_CREATED,
    response_model=AtletaOut
    )

async def post(
    db_session: DatabaseDependency,
    atleta_in: AtletaIn = Body(...)
):
    categoria_nome = atleta_in.categoria.nome
    centro_treinamento_nome = atleta_in.centro_treinamento.nome
    
    categoria = (await db_session.execute(
        select(CategoriaModel).filter_by(nome=categoria_nome)
        )).scalars().first()
    
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"A categoria {categoria_nome} não foi encontrada!"
        )
    
    centro_treinamento = (await db_session.execute(
        select(CentroTreinamentoModel).filter_by(nome=categoria_nome)
        )).scalars().first()
    
    if not centro_treinamento:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"O centro de treinamento {centro_treinamento_nome} não foi encontrado!"
        )
    
    try:
        atleta_out = AtletaOut(id=uuid4(), created_at=datetime.now(timezone.utc), **atleta_in.model_dump())
        atleta_model = AtletaModel(**atleta_out.model_dump(exclude={'categoria'}))
        atleta_model.categoria_id = categoria.pk_id
        atleta_model.centro_treinamento_id = centro_treinamento.pk_id
        
        db_session.add(atleta_model)
        await db_session.commit()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Ocorreu um erro ao inserir os dados no banco!"
        )
    
    return atleta_out
