"""new column users

Revision ID: a48b7e378fdd
Revises: 5e230983c0d1
Create Date: 2023-09-12 11:21:01.495390

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a48b7e378fdd'
down_revision: Union[str, None] = '5e230983c0d1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('username', sa.String(length=60), nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'username')
