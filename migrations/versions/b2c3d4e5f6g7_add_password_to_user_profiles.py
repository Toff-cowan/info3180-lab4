"""Add password to user_profiles

Revision ID: b2c3d4e5f6g7
Revises: a1b2c3d4e5f6
Create Date: 2026-03-11

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2c3d4e5f6g7'
down_revision = 'a1b2c3d4e5f6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('user_profiles', sa.Column('password', sa.String(length=128), nullable=True))


def downgrade():
    op.drop_column('user_profiles', 'password')
