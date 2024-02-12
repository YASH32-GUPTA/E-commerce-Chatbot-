create database Ecommerce ; 
use Ecommerce ; 

-- Create Electronics_Items table with auto-increment
CREATE TABLE Electronics_Items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    Brand_name VARCHAR(50),
    Model_name VARCHAR(50),
    Price DECIMAL(10, 2)
);

-- Insert data manually without specifying item_id
INSERT INTO Electronics_Items (Brand_name, Model_name, Price)
VALUES
    ('Samsung', 'Galaxy S21', 899.99),
    ('Samsung', 'Galaxy Note 20', 1099.99),
    ('Samsung', 'Galaxy A52', 499.99),
    ('Vivo', 'Vivo X60 Pro', 799.99),
    ('Vivo', 'Vivo V21', 599.99),
    ('Vivo', 'Vivo Y20', 299.99),
    ('Apple', 'iPhone 12 Pro', 1199.99),
    ('Apple', 'iPhone SE', 499.99),
    ('Apple', 'iPhone XR', 699.99), 
     ('Samsung', 'Galaxy S21', 899.99),
    ('Samsung', 'Galaxy Note 20', 1099.99),
    ('Samsung', 'Galaxy A52', 499.99),
    ('Samsung', 'Galaxy Z Fold 3', 1799.99),
    ('Samsung', 'Galaxy Buds Pro', 149.99),
    ('Vivo', 'Vivo X60 Pro', 799.99),
    ('Vivo', 'Vivo V21', 599.99),
    ('Vivo', 'Vivo Y20', 299.99),
    ('Vivo', 'Vivo S1 Pro', 349.99),
    ('Vivo', 'Vivo TWS Neo', 129.99),
    ('Apple', 'iPhone 12 Pro', 1199.99),
    ('Apple', 'iPhone SE', 499.99),
    ('Apple', 'iPhone XR', 699.99),
    ('Apple', 'AirPods Pro', 249.99),
    ('Apple', 'iPad Pro 11', 799.99),
    ('Samsung', 'Galaxy S22', 999.99),
    ('Samsung', 'Galaxy Tab S7', 649.99),
    ('Vivo', 'Vivo X70 Pro', 899.99),
    ('Vivo', 'Vivo Y30', 249.99),
    ('Apple', 'iPhone 13 Mini', 699.99),
    ('Apple', 'MacBook Air M1', 999.99);
    
    
Set SQL_SAFE_UPDATES = 0 ; 
update Electronics_Items set price = price*10  ; 
select * from Electronics_Items ; 

