# Write your MySQL query statement below
select a.name as Employee 
from Employee a, Employee b
where a.managerId = b.Id and a.salary > b.salary

