"""new column user

Revision ID: 5e230983c0d1
Revises: c74d21f68864
Create Date: 2023-09-12 11:19:50.899478

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5e230983c0d1'
down_revision: Union[str, None] = 'c74d21f68864'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
