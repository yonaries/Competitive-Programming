# Write your MySQL query statement below
SELECT COALESCE(MAX(salary), null) AS SecondHighestSalary 
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);