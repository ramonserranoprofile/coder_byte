/*
SQL Basic Sum
Your table: maintable_7KICH

MySQL version: 5.5.56-log

In this MySQL challenge, your query should return LastName and the sum of Age from your table for all users with a LastName = Smith. 
The column title of the summed ages should be SumAge. Your output should look like the following table.

*/

/* write your SQL query below */

SELECT LastName, SUM(Age) AS SumAge FROM maintable_7KICH WHERE LastName='Smith' 
