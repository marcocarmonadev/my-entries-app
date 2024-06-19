"""add repeat_interval column

Revision ID: 5ed4405ac1fa
Revises: ee05c59b0e4a
Create Date: 2024-06-19 20:53:50.643288

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "5ed4405ac1fa"
down_revision: Union[str, None] = "ee05c59b0e4a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "entries",
        sa.Column(
            "repeat_interval",
            sa.Integer(),
            nullable=True,
        ),
    )
    op.alter_column(
        "entries",
        "repeated",
        existing_type=sa.BOOLEAN(),
        nullable=True,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("entries", "repeated", existing_type=sa.BOOLEAN(), nullable=False)
    op.drop_column("entries", "repeat_interval")
    # ### end Alembic commands ###
