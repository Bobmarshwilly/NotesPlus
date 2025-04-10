"""Add created_at column to Note

Revision ID: f635545d1b2e
Revises: 1a867b832806
Create Date: 2025-04-08 00:27:21.477480

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f635545d1b2e'
down_revision: Union[str, None] = '1a867b832806'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('notes', sa.Column('created_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('notes', 'created_at')
    # ### end Alembic commands ###
