"""add hotels and rooms tables

Revision ID: 273c52c25d8b
Revises:
Create Date: 2026-09-06 13:27:39.204451

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "273c52c25d8b"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "hotels",
        sa.Column("hotel_id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=200), nullable=False),
        sa.Column("stars", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("hotel_id"),
    )
    op.create_table(
        "rooms",
        sa.Column("room_id", sa.Integer(), nullable=False),
        sa.Column("number", sa.Integer(), nullable=False),
        sa.Column("description", sa.String(length=10000), nullable=False),
        sa.PrimaryKeyConstraint("room_id"),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("rooms")
    op.drop_table("hotels")
