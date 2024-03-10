"""creating project, stage, task, subtask, extension_project, comment

Revision ID: 6c7e434fea22
Revises: b5f8bbf71f6c
Create Date: 2024-03-10 20:03:56.760365

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '6c7e434fea22'
down_revision: Union[str, None] = 'b5f8bbf71f6c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('operation')
    op.drop_table('message')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('message',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('message', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='message_pkey')
    )
    op.create_table('operation',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('quantity', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('figi', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('instrument_type', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('created_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('type', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='operation_pkey')
    )
    # ### end Alembic commands ###
