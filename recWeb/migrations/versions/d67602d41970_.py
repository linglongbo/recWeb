"""empty message

Revision ID: d67602d41970
Revises: b93144e45a60
Create Date: 2020-05-28 19:53:24.889014

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd67602d41970'
down_revision = 'b93144e45a60'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cms_user', sa.Column('_password', sa.String(length=100), nullable=False))
    op.drop_column('cms_user', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cms_user', sa.Column('password', mysql.VARCHAR(length=100), nullable=False))
    op.drop_column('cms_user', '_password')
    # ### end Alembic commands ###