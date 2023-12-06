"""Add foreign key

Revision ID: e72ebc2c0475
Revises: 485cef2a0398
Create Date: 2023-11-13 23:25:36.428523

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e72ebc2c0475'
down_revision: Union[str, None] = '485cef2a0398'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'items', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'items', type_='foreignkey')
    op.drop_column('items', 'user_id')
    # ### end Alembic commands ###