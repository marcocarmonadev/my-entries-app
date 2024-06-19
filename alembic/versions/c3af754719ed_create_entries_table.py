"""create entries table

Revision ID: c3af754719ed
Revises:
Create Date: 2024-06-18 18:28:17.302992

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "c3af754719ed"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "entries",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("amount", sa.Float(), nullable=False),
        sa.Column("creation_date", sa.DateTime(), nullable=False),
        sa.Column("due_date", sa.Date(), nullable=False),
        sa.Column("uuid", sa.Uuid(), nullable=False),
        sa.Column(
            "status",
            sa.Enum(
                "PENDING",
                "COMPLETED",
                "GENERATE_INVOICE",
                "WAITING_INVOICE",
                "CLOSED",
                name="status",
            ),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("entries")
    # ### end Alembic commands ###