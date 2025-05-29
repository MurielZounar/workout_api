from uuid import uuid4

from fastapi import APIRouter, Body, status, HTTPException

from sqlalchemy.future import select

from pydantic import UUID4

from workout_api.contrib.dependencies import DataBaseDependency
from workout_api.centro_treinamento.models import CentroTreinamentoModel
from workout_api.centro_treinamento.schemas import CentroTreinamentoIn, CentroTreinamentoOut


router = APIRouter()

@router.post('/',
             summary='create new centro treinamento',
             status_code=status.HTTP_201_CREATED,
             response_model=CentroTreinamentoOut,
             )
async def post(db_session: DataBaseDependency,
               centro_treinamento_in:CentroTreinamentoIn = Body(...)) -> CentroTreinamentoOut:
    
    ct_in_db = (await db_session.scalar(
    select(CentroTreinamentoModel).where(CentroTreinamentoModel.nome == centro_treinamento_in.nome)
    ))

    if ct_in_db:
        raise HTTPException(status_code=status.HTTP_303_SEE_OTHER, detail="Centro de Treinamento already registered")
    centro_treinamento_out = CentroTreinamentoOut(id=uuid4(), **centro_treinamento_in.model_dump())
    
    centro_treinamento_model = CentroTreinamentoModel(**centro_treinamento_out.model_dump())
    
    db_session.add(centro_treinamento_model)
    await db_session.commit()
    
    
    return centro_treinamento_out


@router.get('/',
             summary='read all centros treinamento',
             status_code=status.HTTP_200_OK,
             response_model=list[CentroTreinamentoOut],
             )
async def query(db_session: DataBaseDependency,) -> list[CentroTreinamentoOut]:
    
    centros_treinamento: list[CentroTreinamentoOut] = (
        await db_session.execute(select(CentroTreinamentoModel))
        ).scalars().all()
    
    return centros_treinamento


@router.get('/{id}',
             summary='read centro treinamento by id',
             status_code=status.HTTP_200_OK,
             response_model=CentroTreinamentoOut,
             )
async def query_id(id:UUID4, db_session: DataBaseDependency,) -> CentroTreinamentoOut:
    
    centro_treinamento_out: CentroTreinamentoOut= (
        await db_session.execute(select(CentroTreinamentoModel).filter_by(id=id))
        ).scalars().first()
    
    if not centro_treinamento_out:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Centro de Treinamento not found by id: {id}')
    
    return centro_treinamento_out