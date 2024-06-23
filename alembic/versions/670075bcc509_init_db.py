"""init_db

Revision ID: 670075bcc509
Revises: 
Create Date: 2024-06-23 13:32:52.244537

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '670075bcc509'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('pk_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.PrimaryKeyConstraint('pk_id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('training_centers',
    sa.Column('pk_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('address', sa.String(length=60), nullable=False),
    sa.Column('owner', sa.String(length=30), nullable=False),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.PrimaryKeyConstraint('pk_id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('athletes',
    sa.Column('pk_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('cpf', sa.String(length=11), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.Column('height', sa.Float(), nullable=False),
    sa.Column('sex', sa.String(length=1), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('training_center_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['categories.pk_id'], ),
    sa.ForeignKeyConstraint(['training_center_id'], ['training_centers.pk_id'], ),
    sa.PrimaryKeyConstraint('pk_id'),
    sa.UniqueConstraint('cpf')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('athletes')
    op.drop_table('training_centers')
    op.drop_table('categories')
    # ### end Alembic commands ###
