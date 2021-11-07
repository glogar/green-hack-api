"""Some description

Revision ID: 568e87d792a5
Revises: 
Create Date: 2021-11-07 03:08:30.517193

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '568e87d792a5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('disease',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('label', sa.String(length=256), nullable=False),
    sa.Column('lon', sa.Float(), nullable=False),
    sa.Column('lat', sa.Float(), nullable=False),
    sa.Column('radius', sa.Integer(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_disease_id'), 'disease', ['id'], unique=False)
    op.create_table('movement',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_lon', sa.Float(), nullable=False),
    sa.Column('start_lat', sa.Float(), nullable=False),
    sa.Column('end_lon', sa.Float(), nullable=False),
    sa.Column('end_lat', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_movement_id'), 'movement', ['id'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=256), nullable=True),
    sa.Column('surname', sa.String(length=256), nullable=True),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=False)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_index(op.f('ix_user_phone'), 'user', ['phone'], unique=False)
    op.create_table('beehive',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('label', sa.String(length=256), nullable=True),
    sa.Column('lon', sa.Float(), nullable=False),
    sa.Column('lat', sa.Float(), nullable=False),
    sa.Column('cluster_id', sa.Integer(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_beehive_id'), 'beehive', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_beehive_id'), table_name='beehive')
    op.drop_table('beehive')
    op.drop_index(op.f('ix_user_phone'), table_name='user')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_movement_id'), table_name='movement')
    op.drop_table('movement')
    op.drop_index(op.f('ix_disease_id'), table_name='disease')
    op.drop_table('disease')
    # ### end Alembic commands ###
