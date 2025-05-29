from uuid import uuid4
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import UUID
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

# Criando a base para os modelos
Base = declarative_base()

# Definindo a classe base com o UUID
class ModelsBaseModel(Base):
    __abstract__ = True
    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), default=uuid4, nullable=False)
