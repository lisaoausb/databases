from lib.item import Item
from lib.database_connection import DatabaseConnection

def test_item_constructs(db_connection):
    item = Item(1, 'dryer', 29.99, 12)
    assert item.id == 1
    assert item.name == 'dryer'
    assert item.unit_price == 29.99
    assert item.stock == 12

def test_equaliser(db_connection):
    item1 = Item(1, 'dryer', 29.99, 12)
    item2 = Item(1, 'dryer', 29.99, 12)
    assert item1 == item2

def test_formatter(db_connection):
    item1 = Item(1, 'dryer', 29.99, 12)
    assert str(item1) == 'Item(1, dryer, 29.99, 12)'