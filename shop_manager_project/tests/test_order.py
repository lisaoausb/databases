from lib.order import Order
from lib.database_connection import DatabaseConnection

def test_item_constructs(db_connection):
    order = Order(1, 'Lisa', '15/05/2023')
    assert order.id == 1
    assert order.customer_name == 'Lisa'
    assert order.date == '15/05/2023'

def test_equaliser(db_connection):
    order1 = Order(1, 'Lisa', '15/05/2023')
    order2 = Order(1, 'Lisa', '15/05/2023')
    assert order1 == order2

def test_formatter(db_connection):
    order = Order(1, 'Lisa', '15/05/2023')
    assert str(order) == 'Order(1, Lisa, 15/05/2023)'