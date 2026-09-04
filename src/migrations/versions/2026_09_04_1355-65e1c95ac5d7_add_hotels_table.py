"""add hotels table

Revision ID: 65e1c95ac5d7
Revises:
Create Date: 2026-09-04 13:55:18.214823

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "65e1c95ac5d7"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "hotels",
        sa.Column("hotel_id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=500), nullable=False),
        sa.Column("stars", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("hotel_id"),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("hotels")
