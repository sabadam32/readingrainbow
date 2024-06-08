"""init

Revision ID: 067315dcd104
Revises: af5fdb4a3416
Create Date: 2024-05-30 12:19:37.291945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '067315dcd104'
down_revision = 'af5fdb4a3416'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('author', sa.String(length=50), nullable=True),
    sa.Column('publish_date', sa.DateTime(), nullable=True),
    sa.Column('category', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_book')),
    sa.UniqueConstraint('title', name=op.f('uq_book_title'))
    )
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mds_number', sa.String(length=10), nullable=True),
    sa.Column('mds_name', sa.String(length=100), nullable=True),
    sa.Column('assigned_name', sa.String(length=100), nullable=True),
    sa.Column('book_count', sa.Integer(), nullable=True),
    sa.Column('last_updated', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_category')),
    sa.UniqueConstraint('mds_number', name=op.f('uq_category_mds_number'))
    )
    op.drop_index('my_index', table_name='models')
    op.drop_table('models')
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('models',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.TEXT(), nullable=True),
    sa.Column('value', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id', name='pk_models')
    )
    op.create_index('my_index', 'models', ['name'], unique=1)
    op.drop_table('category')
    op.drop_table('book')
    # ### end Alembic commands ###
