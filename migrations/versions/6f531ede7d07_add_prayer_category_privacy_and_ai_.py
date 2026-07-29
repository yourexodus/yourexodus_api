"""Add prayer category privacy and AI response

Revision ID: 6f531ede7d07
Revises: aa299c7e02f9
Create Date: 2026-07-25 20:09:04.055707

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f531ede7d07'
down_revision = 'aa299c7e02f9'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('prayers', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'category',
                sa.String(length=50),
                nullable=True
            )
        )

        batch_op.add_column(
            sa.Column(
                'is_private',
                sa.Boolean(),
                nullable=False,
                server_default=sa.false()
            )
        )

        batch_op.add_column(
            sa.Column(
                'ai_response',
                sa.Text(),
                nullable=True
            )
        )
    # ### end Alembic commands ###


def downgrade():
    with op.batch_alter_table('prayers', schema=None) as batch_op:
        batch_op.drop_column('ai_response')
        batch_op.drop_column('is_private')
        batch_op.drop_column('category')

    # ### end Alembic commands ###
