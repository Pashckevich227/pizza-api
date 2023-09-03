"""New collumn

Revision ID: ae1b2835a7a5
Revises: 39913d435fd3
Create Date: 2023-09-03 20:10:08.699484

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ae1b2835a7a5'
down_revision: Union[str, None] = '39913d435fd3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_pizza_id', table_name='pizza')
    op.drop_index('ix_users_id', table_name='users')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=30), autoincrement=False, nullable=False),
    sa.Column('telephone', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('city', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('street', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('house', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('room', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='users_pkey')
    )
    op.create_index('ix_users_id', 'users', ['id'], unique=False)
    op.create_table('pizza',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=30), autoincrement=False, nullable=False),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('size', sa.VARCHAR(length=1), autoincrement=False, nullable=False),
    sa.Column('price', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='pizza_pkey')
    )
    op.create_index('ix_pizza_id', 'pizza', ['id'], unique=False)
    # ### end Alembic commands ###
