"""add cleaned subject

Revision ID: 486c7fa5b533
Revises: 1d7a72222b7c
Create Date: 2015-03-10 16:33:41.740387

"""

# revision identifiers, used by Alembic.
revision = '486c7fa5b533'
down_revision = 'c77a90d524'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('thread', sa.Column('_cleaned_subject',
                                      sa.String(length=255), nullable=True))
    op.create_index('ix_cleaned_subject', 'thread',
                    ['namespace_id', '_cleaned_subject'], unique=False)


def downgrade():
    op.drop_index('ix_cleaned_subject', table_name='thread')
    op.drop_column('thread', '_cleaned_subject')
