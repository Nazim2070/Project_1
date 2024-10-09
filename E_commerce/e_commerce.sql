CREATE DATABASE project;
USE project;
SHOW TABLES ;
CREATE TABLE customers_1 (
customer_id varchar(10) NOT NULL,
name varchar(100) NOT NULL,
city varchar(65) NOT NULL,
email varchar(45) NOT NULL,
phone_no varchar(15) NOT NULL,
address varchar(100) NOT NULL,
pin_code int NOT NULL,
PRIMARY KEY (customer_id)
) ;

INSERT INTO customers_1 (customer_id, name, city, email, phone_no, address, pin_code)
 VALUES
('C1001', 'Steve', 'Tokyo', 'steve@gmail.com', '4567897652', 'f.g.road', '99'),
('C1002', 'John', 'Sydney', 'john@gmail.com', '9987234567', 'k.c.road', '75001'),
('C1003', 'Peter', 'Kanagawa', 'peter.parker@mail.com', '9969834567', '2F Ikenobecho', '171'),
('C1004', 'Jackson', 'Tokyo', 'Jackson@gmail.com', '7756834567', '24-2, Sendagaya', '8429'),
('C1005', 'Jack', 'Lake Buena Vista', 'Jack@gmail.com', '8876345678', '1520 E Buena Vista Drive', '32830'),
('C1006', 'David White', 'Hyderabad', 'david@example.com', '9876543215', '1516 Birch Road', 500001),
('C1007', 'Emma Black', 'Pune', 'emma@example.com', '9876543216', '1718 Spruce Boulevard', 411001),
('C1008', 'Frank Blue', 'Ahmedabad', 'frank@example.com', '9876543217', '1920 Fir Street', 380001),
('C1009', 'Grace Yellow', 'Surat', 'grace@example.com', '9876543218', '2122 Palm Avenue', 395001),
('C1010', 'Hank Red', 'Jaipur', 'hank@example.com', '9876543219', '2324 Elm Crescent', 302001);


CREATE TABLE products_1 (
    product_id VARCHAR(10) PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    sub_category VARCHAR(50),
    original_price DECIMAL(10, 2),
    selling_price DECIMAL(10, 2),
    stock INT
);

INSERT INTO products_1 (product_id, product_name, category, sub_category, original_price, selling_price, stock) 
VALUES
('P101', 'Laptop', 'Electronics', 'Computers', 50000, 45000, 10),
('P102', 'Chair', 'furniture', 'Chairs', 20000, 15000, 10),
('P103', 'Laptop', 'Electronics', 'computer', 60000, 55000, 50),
('P104', 'Smartphone', 'Electronics', 'phone', 45000, 40000, 20),
('P105', 'Blender', 'Appliance', 'Electronics', 500, 450, 10),
('P106', 'Laptop HP', 'Electronics', 'Computers', 67200, 55009, 50),
('P107', 'Mouse', 'Electronics', 'Accessories', 500, 450, 40),
('P108', 'Smartwatch', 'Electronics', 'Wearables', 10000, 9000, 25),
('P109', 'Printer', 'Electronics', 'Computers', 8000, 7200, 18),
('P110', 'Camera', 'Electronics', 'Photography', 35000, 31500, 8);


CREATE TABLE orders_1 (
    order_id INT PRIMARY KEY,
    customer_id VARCHAR(10),
    product_id VARCHAR(10),
    quantity DECIMAL(10, 2),
    total_price DECIMAL(10, 2),
    payment_mode VARCHAR(20),
    order_date DATE,
    order_status VARCHAR(20),
    FOREIGN KEY (customer_id) REFERENCES customers_1(customer_id),
    FOREIGN KEY (product_id) REFERENCES products_1(product_id)
);

INSERT INTO orders_1 (order_id, customer_id, product_id, quantity, total_price, payment_mode, order_date, order_status) 
VALUES
(1, 'C1004', 'P102', 1, 1000, 'COD', '2023-11-30', 'Pending'),
(2,'C1001', 'P101', 1, 45000, 'Credit Card', '2024-10-05', 'Shipped'),
(3,'C1002', 'P102', 2, 54000, 'Debit Card', '2024-10-05', 'Pending'),
(4,'C1003', 'P103', 5, 9000, 'PayPal', '2024-10-05', 'Shipped'),
(5, 'C1005', 'P102', 1, 20000, 'COD', '2023-11-30', 'Pending'),
(6, 'C1005', 'P102', 1, 20000, 'COD', '2023-12-08', 'Shipped'),
(7, 'C1003', 'P103', 1, 55000, 'COD', '2023-12-15', 'Shipped'),
(8, 'C1002', 'P102', 1, 15000, 'COD', '2023-12-01', 'Shipped'),
(9,'C1009', 'P109', 2, 14400, 'Credit Card', '2024-10-05', 'Shipped'),
(10,'C1010', 'P110', 1, 31500, 'Cash on Delivery', '2024-10-05', 'Pending');

SELECT * FROM customers_1;
SELECT * FROM products_1;
SELECT * FROM orders_1;