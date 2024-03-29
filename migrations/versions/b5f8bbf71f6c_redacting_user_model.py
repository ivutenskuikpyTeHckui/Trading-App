"""Redacting User model

Revision ID: b5f8bbf71f6c
Revises: 71a244dc0320
Create Date: 2024-03-08 16:24:20.302744

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b5f8bbf71f6c'
down_revision: Union[str, None] = '71a244dc0320'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_project_manager', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'is_project_manager')
    # ### end Alembic commands ###
