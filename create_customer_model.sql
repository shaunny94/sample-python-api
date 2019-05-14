

/*Select youngest customers */
SELECT name FROM 
customers 
WHERE 
dob = (SELECT MIN(dob) FROM customers) ;