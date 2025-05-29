from uuid import uuid4

from datetime import datetime
from fastapi import APIRouter, Body, status, HTTPException
from sqlalchemy.future import select

from pydantic import UUID4

from workout_api.centro_treinamento.models import CentroTreinamentoModel
from workout_api.categorias.models import CategoriaModel
from workout_api.contrib.dependencies import DataBaseDependency
from workout_api.atleta.schemas import AtletaIn, AtletaOut, AtletaUpdate, AtletaPublic
from workout_api.atleta.models import AtletaModel
from workout_api.contrib.schemas import Message

router = APIRouter()

@router.post('/',
             summary='/create atleta',
             status_code=status.HTTP_201_CREATED,
             response_model=AtletaOut)
async def post(db_session: DataBaseDependency,
               atleta_in: AtletaIn = Body(...)):
    
    atleta_in_db = (await db_session.scalar(
        select(AtletaModel).where(AtletaModel.cpf == atleta_in.cpf)
        ))

    if atleta_in_db:
        raise HTTPException(status_code=status.HTTP_303_SEE_OTHER, detail="Atleta already registered with this CPF")
    
    categoria = (
        await db_session.execute(
            select(CategoriaModel).filter_by(nome=atleta_in.categoria.nome)
        )
    ).scalars().first()
    
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria not found")
    
    
    centro_treinamento = (
        await db_session.execute(
            select(CentroTreinamentoModel).filter_by(nome=atleta_in.centro_treinamento.nome)
        )
    ).scalars().first()

    if not centro_treinamento:
        raise HTTPException(status_code=404, detail="Centro de treinamento not found")
    
    
    atleta_out = AtletaOut(
        id=uuid4(),
        created_at=datetime.utcnow(),
        **atleta_in.model_dump(),
        )
    
    # atleta_model = AtletaModel(**atleta_out.model_dump())
    atleta_model = AtletaModel(
        id=atleta_out.id,
        nome=atleta_out.nome,
        cpf=atleta_out.cpf,
        idade=atleta_out.idade,
        peso=atleta_out.peso,
        altura=atleta_out.altura,
        sexo=atleta_out.sexo,
        created_at=atleta_out.created_at,
        categoria_id=categoria.pk_id,
        centro_treinamento_id=centro_treinamento.pk_id,
    )

    db_session.add(atleta_model)
    await db_session.commit()
    
    return atleta_out


@router.get('/',
             summary='read atletas',
             status_code=status.HTTP_200_OK,
             response_model=list[AtletaPublic],
             )
async def query(db_session: DataBaseDependency,
                nome:str | None = None,
                cpf:str | None = None,
                limit:int = 10,
                skip: int=0) -> list[AtletaPublic]:
    
    query = select(AtletaModel)
    
    if nome:
        query = query.where(AtletaModel.nome.contains(nome))
    if cpf:
        query = query.where(AtletaModel.cpf.contains(cpf))
    
    atletas: list[AtletaPublic] = (await db_session.scalars(query.limit(limit).offset(skip))).all()
    
    return [AtletaPublic.model_validate(atleta) for atleta in atletas]


@router.get('/{id}',
             summary='read atleta by id',
             status_code=status.HTTP_200_OK,
             response_model=AtletaOut,
             )
async def query_id(id:UUID4, db_session: DataBaseDependency,) -> AtletaOut:
    
    atleta: AtletaOut= (
        await db_session.execute(select(AtletaModel).filter_by(id=id))
        ).scalars().first()
    
    if not atleta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Atleta not found by id: {id}')
    
    return atleta



@router.patch('/{id}',
             summary='update atleta by id',
             status_code=status.HTTP_200_OK,
             response_model=AtletaOut,
             )
async def query_id(id:UUID4, db_session: DataBaseDependency, atleta_up: AtletaUpdate = Body(...)) -> AtletaOut:
    
    atleta: AtletaOut= (
        await db_session.execute(select(AtletaModel).filter_by(id=id))
        ).scalars().first()
    
    if not atleta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Atleta not found by id: {id}')
    
    atleta_update = atleta_up.model_dump(exclude_unset=True)
    for key, value in atleta_update.items():
        setattr(atleta, key, value)
        
    await db_session.commit()
    await db_session.refresh(atleta)
    
    
    return atleta



@router.delete('/{id}',
             summary='delete atleta by id',
             status_code=status.HTTP_200_OK,
             response_model=Message,
             )
async def query_id(id:UUID4, db_session: DataBaseDependency,) -> None:
    
    atleta: AtletaOut= (
        await db_session.execute(select(AtletaModel).filter_by(id=id))
        ).scalars().first()
    
    if not atleta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Atleta not found by id: {id}')
    
    await db_session.delete(atleta)
    await db_session.commit()
    
    
    return {'message': 'atleta has been deleted successfully.'}