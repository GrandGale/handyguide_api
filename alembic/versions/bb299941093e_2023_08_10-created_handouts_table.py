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
        sa.Column("title", sa.String(100)),
        sa.Column("url", sa.String(100), default="/"),
        sa.Column("upload_date", sa.DateTime, default=sa.func.now()),
        sa.Column("university", sa.String(100)),
        sa.Column("faculty", sa.String(100)),
        sa.Column("department", sa.String(100)),
        sa.Column("course", sa.String(100)),
        sa.Column("session", sa.String(100), default=settings.SESSION),
    )


def downgrade() -> None:
    op.drop_table("handouts")
