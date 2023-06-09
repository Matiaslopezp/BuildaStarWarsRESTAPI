"""empty message

Revision ID: e82d80d30670
Revises: aeb85538527b
Create Date: 2023-03-14 02:32:31.455289

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e82d80d30670'
down_revision = 'aeb85538527b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fav_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_fav', sa.String(length=120), nullable=True),
    sa.ForeignKeyConstraint(['user_fav'], ['user.email'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fav_user')
    # ### end Alembic commands ###
