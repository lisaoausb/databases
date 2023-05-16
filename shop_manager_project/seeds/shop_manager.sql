-- EXAMPLE
-- (file: spec/seeds_{table_name}.sql)

-- Write your SQL seed here. 

-- First, you'd need to truncate the table - this is so our table is emptied between each test run,
-- so we can start with a fresh state.
-- (RESTART IDENTITY resets the primary key)

DROP TABLE IF EXISTS items_orders; -- replace with your own table name.
DROP TABLE IF EXISTS items; -- replace with your own table name.
DROP TABLE IF EXISTS orders; -- replace with your own table name.

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name text,
    unit_price int,
    stock int
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_name text,
    date text
);

CREATE TABLE items_orders (
    item_id int,
    order_id int,
    constraint fk_item foreign key(item_id) references items(id) on delete cascade,
    constraint fk_order foreign key(order_id) references orders(id) on delete cascade,
    PRIMARY KEY (item_id, order_id)
);
-- Below this line there should only be `INSERT` statements.
-- Replace these statements with your own seed data.

