"""created faculties table

Revision ID: 31a0e3f46050
Revises: 83b94a4fea5a
Create Date: 2023-08-10 22:13:59.137209

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "31a0e3f46050"
down_revision = "83b94a4fea5a"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "faculties",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(100)),
        sa.Column("abbrev", sa.String(10), index=True),
        sa.Column("university", sa.String),
        sa.ForeignKeyConstraint(
            ["university"], ["universities.abbrev"], ondelete="CASCADE"
        ),
        sa.UniqueConstraint("name", "university", name="unique_faculty"),
    )


def downgrade() -> None:
    op.drop_table("faculties")
