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
        sa.Column("name", sa.String(100)),
        sa.Column("code", sa.String(10), index=True),
        sa.Column("level", sa.String),
        sa.Column("department", sa.String),
        sa.Column("faculty", sa.String),
        sa.Column("university", sa.String),
        sa.ForeignKeyConstraint(["level"], ["levels.name"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(
            ["department"], ["departments.abbrev"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(["faculty"], ["faculties.abbrev"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(
            ["university"], ["universities.abbrev"], ondelete="CASCADE"
        ),
        sa.UniqueConstraint("name", "code", "university", name="unique_course"),
    )


def downgrade() -> None:
    op.drop_table("courses")
