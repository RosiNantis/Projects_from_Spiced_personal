
-- which of our customers never made any orders?

SELECT companyname
FROM 
orders ord RIGHT JOIN customers cus
ON ord.customerid = cus.customerid
WHERE orderid IS NULL;


--What is the average weight of all the orders, delivered to each country?
	-- e.g. 500 kg to Germany, 250 kg to Spain

SELECT cus.country, ROUND(AVG(ord.freight)) AS weight
FROM orders ord 
INNER JOIN
customers cus
ON ord.customerid = cus.customerid
GROUP BY cus.country
ORDER BY weight DESC;


-- What is the total revenue delivered to each country?
   -- e.g. total money made from all orders to each country
--
SELECT SUM(det.unitprice * det.quantity * (1 - det.discount)) AS revenue, cus.country
FROM order_details det
    -- a double join!!
	INNER JOIN orders ord
	ON det.orderid = ord.orderid
	INNER JOIN customers cus
	ON ord.customerid = cus.customerid
GROUP BY cus.country
ORDER BY revenue DESC;


-- DROP PRIMARY KEY
alter table customers drop constraint cust_pk;


-- PRIMARY KEY
alter table customers 
add constraint cust_pk
primary key (customerid);

-- drop primary
alter table orders drop constraint ord_pk;

-- explain
explain analyze select orderid from orders where orderid = '10905';

-- PRIMARY KEY
alter table orders 
add constraint ord_pk
primary key (orderid);

-- explain
explain analyze select orderid from orders where orderid = '10905';



-- FOREIGN KEY 
ALTER TABLE orders
ADD CONSTRAINT fk_cust
FOREIGN KEY (customerid)
REFERENCES customers(customerid);


select * from orders;

-- this will fail because there is no customer with this record
INSERT INTO orders VALUES (999, 'COLIM', 999);

-- after adding the customer record, this will work
insert into customers values ('COLIM');
INSERT INTO orders VALUES (999, 'COLIM', 999);

-- check the new record
select * from orders where customerid = 'COLIM';

--
-- this would fail 
delete from customers where customerid = 'COLIM';

-- delete first from orders 
delete from orders where customerid = 'COLIM';
delete from customers where customerid = 'COLIM';   


-- drop the foreign constraint
ALTER TABLE orders DROP CONSTRAINT fk_cust;

-- create a new constraint
ALTER TABLE orders
ADD CONSTRAINT fk_cust
FOREIGN KEY (customerid)
REFERENCES customers(customerid)
on delete cascade ;

-- add the records again
insert into customers values ('COLIM');
INSERT INTO orders VALUES (999, 'COLIM', 999);

-- try deleting now the record from the table
delete from customers where customerid = 'COLIM';

-- select again from the orders, because delete was cascaded
select * from orders where customerid = 'COLIM';

-- drop the foreign constraint
ALTER TABLE orders DROP CONSTRAINT fk_cust;


