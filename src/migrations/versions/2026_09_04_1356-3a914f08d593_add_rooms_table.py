"""add rooms table

Revision ID: 3a914f08d593
Revises: 65e1c95ac5d7
Create Date: 2026-09-04 13:56:27.993502

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "3a914f08d593"
down_revision: str | Sequence[str] | None = "65e1c95ac5d7"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
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
