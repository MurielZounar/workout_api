"""Criando do zero as coisas

Revision ID: c38e5d987a1f
Revises: 
Create Date: 2025-01-23 11:58:27.299130

"""
from typing import Sequence, Union
import uuid
from alembic import op
import sqlalchemy as sa

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
# revision identifiers, used by Alembic.
revision: str = 'c38e5d987a1f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    # Tabela de Categorias
    op.create_table(
        'categorias',
        sa.Column('pk_id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False),
        sa.Column('nome', sa.String(length=50), nullable=False),
        sa.Column('id', UUID(as_uuid=True), nullable=False),
        sa.PrimaryKeyConstraint('pk_id'),
        sa.UniqueConstraint('nome')
    )

    # Tabela de Centros de Treinamento
    op.create_table(
        'centros_treinamento',
        sa.Column('pk_id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False),
        sa.Column('nome', sa.String(length=50), nullable=False),
        sa.Column('endereco', sa.String(length=60), nullable=False),
        sa.Column('proprietario', sa.String(length=30), nullable=False),
        sa.Column('id', UUID(as_uuid=True), nullable=False),
        sa.PrimaryKeyConstraint('pk_id'),
        sa.UniqueConstraint('nome')
    )

    # Tabela de Atletas
    op.create_table(
        'atletas',
        sa.Column('pk_id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False),
        sa.Column('nome', sa.String(length=50), nullable=False),
        sa.Column('cpf', sa.String(length=11), nullable=False),
        sa.Column('idade', sa.Integer(), nullable=False),
        sa.Column('peso', sa.Float(), nullable=False),
        sa.Column('altura', sa.Float(), nullable=False),
        sa.Column('sexo', sa.String(length=1), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('categoria_id', UUID(as_uuid=True), nullable=False),
        sa.Column('centro_treinamento_id', UUID(as_uuid=True), nullable=False),
        sa.Column('id', UUID(as_uuid=True), nullable=False),
        sa.ForeignKeyConstraint(['categoria_id'], ['categorias.pk_id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['centro_treinamento_id'], ['centros_treinamento.pk_id'], ondelete='CASCADE'),
        sa.UniqueConstraint('cpf')
    )

def downgrade():
    op.drop_table('atletas')
    op.drop_table('centros_treinamento')
    op.drop_table('categorias')