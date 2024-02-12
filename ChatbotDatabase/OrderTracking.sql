use Ecommerce ; 

-- Create OrdersTracking table
CREATE TABLE OrdersTracking (
    order_id INT,
    Status VARCHAR(20),
    PRIMARY KEY (order_id, item_id),
    FOREIGN KEY (order_id, item_id) REFERENCES Orders(order_id, item_id)
);

-- Insert data manually into OrdersTracking
INSERT INTO OrdersTracking (order_id, item_id, Status)
VALUES
    (101, 1, 'delivered'),
    (101, 2, 'intransit'),
    (102, 3, 'ready'),
    (102, 1, 'intransit'),
    (103, 2, 'delivered'),
    (104, 1, 'ready'),
    (104, 3, 'intransit'),
    (105, 2, 'ready'),
    (106, 1, 'delivered'),
    (106, 2, 'intransit');



select * from 
Orders 
natural join OrdersTracking ; 


Select * from OrdersTracking ; 