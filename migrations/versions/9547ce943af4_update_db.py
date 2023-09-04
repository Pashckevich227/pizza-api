"""Update db

Revision ID: 9547ce943af4
Revises: ae1b2835a7a5
Create Date: 2023-09-04 21:11:04.971603

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9547ce943af4'
down_revision: Union[str, None] = 'ae1b2835a7a5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_pizza_id'), 'pizza', ['id'], unique=False)
    op.add_column('users', sa.Column('email', sa.String(length=60), nullable=True))
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_column('users', 'email')
    op.drop_index(op.f('ix_pizza_id'), table_name='pizza')
    # ### end Alembic commandss ###
