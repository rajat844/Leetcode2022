# Write your MySQL query statement below
# select ConsecutiveNums 
# from (
#     select distinct num as ConsecutiveNums , lead(num,1) over() as num_1 ,lead(num,2) over() as num_2
#     from Logs
#     ) t
# where t.num_1 = t.num_2 and t.num_1 = ConsecutiveNums

select distinct a.num as ConsecutiveNums
from logs a
join logs b on a.id = b.id + 1 and a.num = b.num
join logs c on a.id = c.id + 2 and a.num = c.num