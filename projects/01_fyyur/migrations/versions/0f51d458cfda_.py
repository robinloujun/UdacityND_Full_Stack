"""empty message

Revision ID: 0f51d458cfda
Revises: 5a37af4cd1ab
Create Date: 2021-01-12 17:06:05.527386

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f51d458cfda'
down_revision = '5a37af4cd1ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shows', sa.Column('end_time', sa.DateTime(), nullable=False))
    
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('shows', 'end_time')
    # ### end Alembic commands ###
