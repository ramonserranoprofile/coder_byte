/* SQL Contains Letter

Your table: maintable_RXG99
MySQL version: 5.5.56-log

In this MySQL challenge, 
your query should return the number of rows from your table where FirstName contains "e" and LastName has more than 5 characters. 
Your output should look like the following table.  */


SELECT COUNT(*)
FROM maintable_RXG99
WHERE FirstName like '%e%' AND LENGTH(LastName) > 5