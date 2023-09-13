"""delete columns user

Revision ID: e255655e06a3
Revises: a48b7e378fdd
Create Date: 2023-09-12 12:14:18.952215

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e255655e06a3'
down_revision: Union[str, None] = 'a48b7e378fdd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('users', 'first_name')
    op.drop_column('users', 'second_name')
    op.drop_column('users', 'telephone')
    op.drop_column('users', 'city')
    op.drop_column('users', 'street')
    op.drop_column('users', 'house')
    op.drop_column('users', 'room')


def downgrade() -> None:
    op.add_column('users', sa.Column('first_name', sa.String(length=30), nullable=False))
    op.add_column('users', sa.Column('second_name', sa.String(length=40), nullable=False))
    op.add_column('users', sa.Column('telephone', sa.String(length=30), nullable=True))
    op.add_column('users', sa.Column('city', sa.String(length=30), nullable=True))
    op.add_column('users', sa.Column('street', sa.String(length=100), nullable=True))
    op.add_column('users', sa.Column('house', sa.INTEGER(), nullable=True))
    op.add_column('users', sa.Column('room', sa.INTEGER(), nullable=True))

