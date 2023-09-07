"""Update user

Revision ID: c74d21f68864
Revises: 9547ce943af4
Create Date: 2023-09-07 19:12:20.796118

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c74d21f68864'
down_revision: Union[str, None] = '9547ce943af4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('first_name', sa.String(length=30), nullable=False))
    op.add_column('users', sa.Column('second_name', sa.String(length=40), nullable=False))
    op.add_column('users', sa.Column('password', sa.String(), nullable=False))
    op.drop_column('users', 'name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('name', sa.VARCHAR(length=30), autoincrement=False, nullable=False))
    op.drop_column('users', 'password')
    op.drop_column('users', 'second_name')
    op.drop_column('users', 'first_name')
    # ### end Alembic commands ###
