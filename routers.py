from fastapi import APIRouter
from fastapitest.atleta.controller import router as atleta
from fastapitest.categorias.controller import router as categoria
from fastapitest.centro_treinamento.controller import router as centro_treinamento

api_router = APIRouter()
api_router.include_router(atleta, prefix='/atletas', tags=['atletas'])
api_router.include_router(categoria, prefix='/categorias', tags=['categorias'])
api_router.include_router(centro_treinamento, prefix='/centro_treinamento', tags=['centro_treinamento'])