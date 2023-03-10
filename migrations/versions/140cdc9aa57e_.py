"""empty message

Revision ID: 140cdc9aa57e
Revises: 
Create Date: 2022-12-31 12:45:45.577871

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '140cdc9aa57e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('price', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('qty', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.drop_column('qty')
        batch_op.drop_column('price')
        batch_op.drop_column('name')

    # ### end Alembic commands ###
