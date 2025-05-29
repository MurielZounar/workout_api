from uuid import uuid4

from workout_api.contrib.models import ModelsBaseModel
from workout_api.atleta.models import AtletaModel

from sqlalchemy import Integer, String, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship


class CentroTreinamentoModel(ModelsBaseModel):
    __tablename__ = 'centros_treinamento'
    
    pk_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    nome: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    endereco: Mapped[str] = mapped_column(String(60), nullable=False)
    proprietario: Mapped[str] = mapped_column(String(30), nullable=False)
    atleta: Mapped[AtletaModel] = relationship(back_populates='centro_treinamento') #isso possívelmente está errado
