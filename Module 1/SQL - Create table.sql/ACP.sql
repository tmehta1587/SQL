
CREATE TABLE CUSTOMERS(
    CUSTOMER_ID TEXT,
    CUSTOMER_NAME TEXT, 
    GRADE INTEGER, 
    COUNTRY TEXT
);

INSERT INTO CUSTOMERS(CUSTOMER_ID, CUSTOMER_NAME, GRADE, COUNTRY) VALUES
    ('1', 'Sam', 98, 'New York'),
    ('2', 'Henry', 101, 'L.A'),
    ('3', 'Tom', 100, 'New York'),
    ('4', 'Smith', 105, 'New York'),
    ('5', 'Harry', 104, 'California');

SELECT CUSTOMER_NAME FROM CUSTOMERS WHERE COUNTRY='New York' OR GRADE>100;

