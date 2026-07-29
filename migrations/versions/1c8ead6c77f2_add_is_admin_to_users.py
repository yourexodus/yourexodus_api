"""Add is_admin to users

Revision ID: 1c8ead6c77f2
Revises: 6f531ede7d07
Create Date: 2026-07-29 09:18:07.831381

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c8ead6c77f2'
down_revision = '6f531ede7d07'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'is_admin',
                sa.Boolean(),
                nullable=False,
                server_default=sa.false()
            )
        )
    # ### end Alembic commands ###


def downgrade():
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('is_admin')

    # ### end Alembic commands ###
