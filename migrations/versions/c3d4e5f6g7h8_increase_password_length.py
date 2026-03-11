"""Increase password column length for hashes

Revision ID: c3d4e5f6g7h8
Revises: b2c3d4e5f6g7
Create Date: 2026-03-11

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3d4e5f6g7h8'
down_revision = 'b2c3d4e5f6g7'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        'user_profiles', 'password',
        existing_type=sa.String(length=128),
        type_=sa.String(length=256),
        existing_nullable=True
    )


def downgrade():
    op.alter_column(
        'user_profiles', 'password',
        existing_type=sa.String(length=256),
        type_=sa.String(length=128),
        existing_nullable=True
    )
