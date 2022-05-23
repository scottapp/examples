"""empty message

Revision ID: e516f5e769df
Revises: 
Create Date: 2022-05-05 10:42:16.117345

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e516f5e769df'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.Unicode(200), nullable=False),
        sa.Column('password', sa.Unicode(200), nullable=False),
        sa.Column('name', sa.String(50)),
        sa.Column('is_active', sa.Boolean),
        sa.Column('created_at', sa.DateTime)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
