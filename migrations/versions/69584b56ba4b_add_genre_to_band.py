"""Add genre to Band

Revision ID: 69584b56ba4b
Revises: 4b4ad425147f
Create Date: 2024-09-28 01:57:11.928254

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision: str = '69584b56ba4b'
down_revision: Union[str, None] = '4b4ad425147f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # Adding the 'genre' column to the 'bands' table
    op.add_column('bands', sa.Column('genre', sa.String(), nullable=True))  # Make genre nullable

def downgrade() -> None:
    # Dropping the 'genre' column from the 'bands' table
    op.drop_column('bands', 'genre')
