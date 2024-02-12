use Ecommerce ; 

CREATE TABLE Orders (
    order_id INT,
    item_id INT,
    quantity INT,
    PRIMARY KEY (order_id, item_id),
    FOREIGN KEY (item_id) REFERENCES Electronics_Items(item_id)
);

-- Insert data manually into Orders
INSERT INTO Orders (order_id, item_id, quantity)
VALUES
    (101, 1, 2),
    (101, 2, 1),
    (102, 3, 3),
    (102, 1, 1),
    (103, 2, 2),
    (104, 1, 1),
    (104, 3, 2),
    (105, 2, 1),
    (106, 1, 3),
    (106, 2, 2);
    
select * from 
Electronics_Items 
natural join orders ; 


select * from orders order by order_id ; 
select item_id from orders where order_id = 111 ; 

SET autocommit = 1;
