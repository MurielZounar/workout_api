from datetime import datetime
from uuid import uuid4

from workout_api.contrib.models import ModelsBaseModel
from workout_api.categorias.models import CategoriaModel
from sqlalchemy import Integer, String, Float, DateTime, ForeignKey, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship


class AtletaModel(ModelsBaseModel):
    __tablename__ = 'atletas'
    
    pk_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    peso: Mapped[float] = mapped_column(Float, nullable=False)
    altura: Mapped[float] = mapped_column(Float, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    categoria: Mapped[CategoriaModel] = relationship(back_populates='atleta', lazy='selectin')
    categoria_id: Mapped[UUID] = mapped_column(ForeignKey('categorias.pk_id'))
    centro_treinamento: Mapped['CentroTreinamentoModel'] = relationship(back_populates='atleta', lazy='selectin') # type: ignore
    centro_treinamento_id: Mapped[UUID] = mapped_column(ForeignKey('centros_treinamento.pk_id'))

    