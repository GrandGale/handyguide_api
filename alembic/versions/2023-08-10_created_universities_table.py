"""create universities table

Revision ID: 83b94a4fea5a
Revises: 
Create Date: 2023-08-10 22:03:17.848847

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "83b94a4fea5a"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "universities",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(100), unique=True),
        sa.Column("abbrev", sa.String(10), unique=True, index=True),
        sa.Column("date_created", sa.DateTime, default=sa.func.now()),
    )


def downgrade() -> None:
    op.drop_table("universities")
