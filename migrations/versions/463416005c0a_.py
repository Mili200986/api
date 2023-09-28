"""empty message

Revision ID: 463416005c0a
Revises: 
Create Date: 2023-09-26 20:42:07.857655

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '463416005c0a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('usuario', sa.String(length=80), nullable=False),
    sa.Column('contraseña', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('usuario')
    )
    with op.batch_alter_table('usuarios', schema=None) as batch_op:
        batch_op.drop_index('nombre_usuario')

    op.drop_table('usuarios')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuarios',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nombre_usuario', mysql.VARCHAR(length=80), nullable=False),
    sa.Column('contraseña', mysql.VARCHAR(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('usuarios', schema=None) as batch_op:
        batch_op.create_index('nombre_usuario', ['nombre_usuario'], unique=False)

    op.drop_table('usuario')
    # ### end Alembic commands ###
