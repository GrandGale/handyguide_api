"""created user table

Revision ID: 422fb07c1975
Revises: bb299941093e
Create Date: 2023-08-15 19:46:00.320652

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "422fb07c1975"
down_revision = "bb299941093e"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "contributors",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("username", sa.String(50), nullable=False, unique=True),
        sa.Column("email", sa.String(120), nullable=False, unique=True),
        sa.Column("first_name", sa.String(20), nullable=False),
        sa.Column("last_name", sa.String(20), nullable=False),
        sa.Column("university_id", sa.String(30), nullable=False),
        sa.Column("university", sa.String(10), nullable=False),
        sa.Column("level", sa.String(10), nullable=False),
        sa.Column("faculty", sa.Integer, nullable=False),
        sa.Column("department", sa.Integer, nullable=False),
        sa.Column("password", sa.String(50), nullable=False),
        sa.Column("is_active", sa.Boolean, nullable=False, default=True),
        sa.Column("is_contributor", sa.Boolean, nullable=False, default=False),
        sa.Column("is_supervisor", sa.Boolean, nullable=False, default=False),
        sa.Column("is_admin", sa.Boolean, nullable=False, default=False),
        sa.Column("last_login", sa.DateTime, nullable=False),
        sa.Column("created_at", sa.DateTime, nullable=False, default=sa.func.now()),
        sa.ForeignKeyConstraint(
            ["university"], ["universities.abbrev"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(["faculty"], ["faculties.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["department"], ["departments.id"], ondelete="CASCADE"),
        sa.UniqueConstraint(
            "university_id",
            "university",
            "level",
            "faculty",
            "department",
            name="unique_contributor",
        ),
    )


def downgrade() -> None:
    op.drop_table("contributors")
