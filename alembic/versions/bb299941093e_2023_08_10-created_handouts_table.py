"""created handouts table

Revision ID: bb299941093e
Revises: ee810aafdb2c
Create Date: 2023-08-10 23:20:00.758526

"""
from alembic import op
import sqlalchemy as sa

from app.config.settings import settings


# revision identifiers, used by Alembic.
revision = "bb299941093e"
down_revision = "ee810aafdb2c"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "handouts",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("title", sa.String(100), nullable=False),
        sa.Column("url", sa.String(100), default="/", nullable=False),
        sa.Column("upload_date", sa.DateTime, default=sa.func.now(), nullable=False),
        sa.Column("university", sa.String, nullable=False),
        sa.Column("faculty", sa.Integer, nullable=False),
        sa.Column("department", sa.Integer, nullable=False),
        sa.Column("course", sa.Integer, nullable=False),
        sa.Column("session", sa.String(100), default=settings.SESSION, nullable=False),
        sa.Column("level", sa.String, nullable=False),
        sa.ForeignKeyConstraint(
            ["university"], ["universities.abbrev"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(["faculty"], ["faculties.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["department"], ["departments.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["course"], ["courses.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["level"], ["levels.abbrev"], ondelete="CASCADE"),
        sa.UniqueConstraint("title", "course", "level", name="unique_handout"),
    )


def downgrade() -> None:
    op.drop_table("handouts")
