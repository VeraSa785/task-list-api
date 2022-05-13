"""empty message

Revision ID: 01f8a354bf75
Revises: 
Create Date: 2022-05-12 17:08:39.355504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01f8a354bf75'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('goal',
    sa.Column('goal_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('goal_id')
    )
    op.create_table('task',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('completed_at', sa.DateTime(), nullable=True),
    sa.Column('goal_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['goal_id'], ['goal.goal_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('task')
    op.drop_table('goal')
    # ### end Alembic commands ###