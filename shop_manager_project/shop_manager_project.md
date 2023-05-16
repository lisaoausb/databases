As a shop manager
So I can know which items I have in stock
I want to keep a list of my shop items with their name and unit price.

As a shop manager
So I can know which items I have in stock
I want to know which quantity (a number) I have for each item.

As a shop manager
So I can manage items
I want to be able to create a new item.

As a shop manager
So I can know which orders were made
I want to keep a list of orders with their customer name.

As a shop manager
So I can know which orders were made
I want to assign each order to their corresponding item.

As a shop manager
So I can know which orders were made
I want to know on which date an order was placed. 

As a shop manager
So I can manage orders
I want to be able to create a new order.

nouns: items, item name, item unit price, stock per item, orders, customer name, date

Record  Properties
item    name, unit price, stock
order   customer_name, date

first table: items
second table: orders

table name: items
id SERIAL PRIMARY KEY
name text
unit_price int
stock int

table name: orders
id SERIAL PRIMARY KEY
customer_name text
date text

table name: items_orders
item_id int
order_id int

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
    contraint fk_item foreign key(item_id) references items(id) on delete cascade,
    constraint fk_order foreign key(order_id) references orders(id) on delete cascade,
    PRIMARY KEY (item_id, order_id)
);

psql -h 127.0.0.1 shop_manager < shop_manager.sql


Can items have many orders? YES
Can orders have many items? YES