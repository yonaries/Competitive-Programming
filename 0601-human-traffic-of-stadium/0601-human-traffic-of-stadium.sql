# Write your MySQL query statement below
SELECT id, visit_date, people
FROM stadium
WHERE people>=100
AND 
(
    (id+1 IN (SELECT id FROM stadium WHERE people>=100)     -- first row
    AND id+2 IN (SELECT id FROM stadium WHERE people>=100))
OR 
    (id+1 IN (SELECT id FROM stadium WHERE people>=100)     -- middle row
    AND id-1 IN (SELECT id FROM stadium WHERE people>=100))
OR
    (id-1 IN (SELECT id FROM stadium WHERE people>=100)     -- last row
     AND id-2 IN (SELECT id FROM stadium WHERE people>=100)));