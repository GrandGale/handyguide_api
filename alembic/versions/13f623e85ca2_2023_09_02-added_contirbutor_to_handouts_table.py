"""added contirbutor to handouts table

Revision ID: 13f623e85ca2
Revises: 422fb07c1975
Create Date: 2023-09-02 12:50:52.310972

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "13f623e85ca2"
down_revision = "422fb07c1975"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "handouts",
        sa.Column("contributor", sa.Integer, nullable=False),
    )


def downgrade() -> None:
    op.drop_column("handouts", "contributor")
