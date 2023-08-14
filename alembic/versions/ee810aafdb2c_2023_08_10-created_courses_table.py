"""created courses table

Revision ID: ee810aafdb2c
Revises: f47d2883f842
Create Date: 2023-08-10 23:13:17.873789

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "ee810aafdb2c"
down_revision = "f47d2883f842"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "courses",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("code", sa.String(10), index=True, nullable=False),
        sa.Column("level", sa.String, nullable=False),
        sa.Column("department", sa.Integer, nullable=False),
        sa.Column("faculty", sa.Integer, nullable=False),
        sa.Column("university", sa.String, nullable=False),
        sa.ForeignKeyConstraint(["level"], ["levels.abbrev"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["department"], ["departments.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["faculty"], ["faculties.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(
            ["university"], ["universities.abbrev"], ondelete="CASCADE"
        ),
        sa.UniqueConstraint("name", "code", "university", name="unique_course"),
    )


def downgrade() -> None:
    op.drop_table("courses")
