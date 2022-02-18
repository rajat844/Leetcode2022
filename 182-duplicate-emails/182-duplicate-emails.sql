# Write your MySQL query statement below
select Email from (select email as Email , count(email) as c
from Person group by email)t
where c > 1
