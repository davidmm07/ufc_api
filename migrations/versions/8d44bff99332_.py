"""empty message

Revision ID: 8d44bff99332
Revises: 
Create Date: 2024-04-06 18:51:37.275711

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d44bff99332'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fighter',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('skills', sa.String(length=200), nullable=False),
    sa.Column('weaknesses', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fight',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fighter1_id', sa.Integer(), nullable=False),
    sa.Column('fighter2_id', sa.Integer(), nullable=False),
    sa.Column('winner_id', sa.Integer(), nullable=True),
    sa.Column('loser_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['fighter1_id'], ['fighter.id'], ),
    sa.ForeignKeyConstraint(['fighter2_id'], ['fighter.id'], ),
    sa.ForeignKeyConstraint(['loser_id'], ['fighter.id'], ),
    sa.ForeignKeyConstraint(['winner_id'], ['fighter.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fight')
    op.drop_table('fighter')
    # ### end Alembic commands ###
