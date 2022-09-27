"""empty message

Revision ID: 2646f0481e7e
Revises: 8b348cb5fa6c
Create Date: 2022-09-22 15:49:07.562624

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2646f0481e7e'
down_revision = '8b348cb5fa6c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.String(length=120), nullable=False))
    op.create_unique_constraint(None, 'user', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'username')
    # ### end Alembic commands ###
