# Write your MySQL query statement below
select ConsecutiveNums 
from (
    select distinct num as ConsecutiveNums , lead(num,1) over() as num_1 ,lead(num,2) over() as num_2
    from Logs
    ) t
where t.num_1 = t.num_2 and t.num_1 = ConsecutiveNums