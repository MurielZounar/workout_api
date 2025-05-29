from uuid import uuid4

from workout_api.contrib.models import ModelsBaseModel


from sqlalchemy import Integer, String, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship


class CategoriaModel(ModelsBaseModel):
    __tablename__ = 'categorias'
    
    pk_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    nome: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    atleta: Mapped['AtletaModel'] = relationship('AtletaModel',back_populates='categoria') # type: ignore
