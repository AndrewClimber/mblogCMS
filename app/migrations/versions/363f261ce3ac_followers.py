"""followers

Revision ID: 363f261ce3ac
Revises: 320209d15d40
Create Date: 2018-12-13 16:12:24.175483

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '363f261ce3ac'
down_revision = '320209d15d40'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
