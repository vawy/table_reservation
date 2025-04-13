"""reservation restaurant table models

Revision ID: 211d0ed1d89e
Revises: 
Create Date: 2025-04-09 19:16:40.345365

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '211d0ed1d89e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('restaurant_table',
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('seats', sa.SmallInteger(), nullable=False),
    sa.Column('location', sa.String(length=100), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.CheckConstraint('seats > 0', name='check_seats_positive'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_restaurant_table_location'), 'restaurant_table', ['location'], unique=False)
    op.create_index(op.f('ix_restaurant_table_name'), 'restaurant_table', ['name'], unique=True)
    op.create_table('reservation',
    sa.Column('customer_name', sa.String(length=100), nullable=False),
    sa.Column('restaurant_table_id', sa.Integer(), nullable=False),
    sa.Column('reservation_time', sa.DateTime(timezone=True), nullable=False),
    sa.Column('duration_minutes', sa.SmallInteger(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['restaurant_table_id'], ['restaurant_table.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('idx_reservation_table_time', 'reservation', ['restaurant_table_id', 'reservation_time'], unique=False)
    op.create_index(op.f('ix_reservation_customer_name'), 'reservation', ['customer_name'], unique=False)
    op.create_index(op.f('ix_reservation_reservation_time'), 'reservation', ['reservation_time'], unique=False)

    test_restaurant_tables = [
        {
            "name": "Стол1",
            "seats": 5,
            "location": "терраса"
        },
        {
            "name": "Стол2",
            "seats": 2,
            "location": "У окна"
        },
        {
            "name": "Стол3",
            "seats": 3,
            "location": "барная стойка"
        },
        {
            "name": "Стол4",
            "seats": 10,
            "location": "VIP комната"
        },
        {
            "name": "Стол5",
            "seats": 6,
            "location": "крыша"
        }
    ]

    for table in test_restaurant_tables:
        op.execute(
            sa.text("insert into restaurant_table values (:name, :seats, :location)")
            .bindparams(name=table.get("name"), seats=table.get("seats"), location=table.get("location"))
        )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_reservation_reservation_time'), table_name='reservation')
    op.drop_index(op.f('ix_reservation_customer_name'), table_name='reservation')
    op.drop_index('idx_reservation_table_time', table_name='reservation')
    op.drop_table('reservation')
    op.drop_index(op.f('ix_restaurant_table_name'), table_name='restaurant_table')
    op.drop_index(op.f('ix_restaurant_table_location'), table_name='restaurant_table')
    op.drop_table('restaurant_table')
    # ### end Alembic commands ###
