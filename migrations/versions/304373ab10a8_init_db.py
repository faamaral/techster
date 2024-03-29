"""init db

Revision ID: 304373ab10a8
Revises: 
Create Date: 2023-10-18 22:15:34.188637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '304373ab10a8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=25), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('category', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_category_name'), ['name'], unique=True)

    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('slug', sa.String(), nullable=False),
    sa.Column('author', sa.Integer(), nullable=True),
    sa.Column('abstract', sa.Text(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('last_edit', sa.DateTime(), nullable=True),
    sa.Column('category', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author'], ['user.id'], ),
    sa.ForeignKeyConstraint(['category'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))

    op.drop_table('user')
    with op.batch_alter_table('category', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_category_name'))

    op.drop_table('category')
    # ### end Alembic commands ###
