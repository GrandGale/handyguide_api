"""create levels table

Revision ID: f47d2883f842
Revises: 8916184d747c
Create Date: 2023-08-10 23:08:57.296738

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f47d2883f842"
down_revision = "8916184d747c"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "levels",
        sa.Column("name", sa.String(20), unique=True),
        sa.Column("abbrev", sa.String(10), primary_key=True),
    )


def downgrade() -> None:
    op.drop_table("levels")
