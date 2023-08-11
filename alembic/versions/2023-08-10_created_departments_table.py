"""create departments table

Revision ID: 8916184d747c
Revises: 31a0e3f46050
Create Date: 2023-08-10 22:42:20.523268

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "8916184d747c"
down_revision = "31a0e3f46050"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "departments",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("abbrev", sa.String(10), index=True, nullable=False),
        sa.Column("faculty", sa.String, nullable=False),
        sa.Column("university", sa.String, nullable=False),
        sa.ForeignKeyConstraint(["faculty"], ["faculties.abbrev"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(
            ["university"], ["universities.abbrev"], ondelete="CASCADE"
        ),
        sa.UniqueConstraint("name", "faculty", "university", name="unique_department"),
    )


def downgrade() -> None:
    op.drop_table("departments")
