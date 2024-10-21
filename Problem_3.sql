create table products (
    id int PRIMARY KEY,
    name varchar(100),
    price decimal(10, 2)
);
insert into products values
(1, 'A', 1000.00),
(2, 'B', 500.00),
(3, 'C', 300.00),
(4, 'D', 150.00),
(5, 'E', 250.00);
SELECT name, price * 1.10 AS new_price
FROM products;