# Write your MySQL query statement below
SELECT email AS Email
FROM (
    SELECT email, COUNT(*) AS cnt
    FROM Person
    GROUP BY email
     ) t
WHERE cnt > 1;