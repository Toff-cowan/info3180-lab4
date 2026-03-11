"""Create user_profiles table

Revision ID: a1b2c3d4e5f6
Revises:
Create Date: 2026-03-11

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1b2c3d4e5f6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user_profiles',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('first_name', sa.String(length=80), nullable=True),
        sa.Column('last_name', sa.String(length=80), nullable=True),
        sa.Column('username', sa.String(length=80), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('username')
    )


def downgrade():
    op.drop_table('user_profiles')
