# Write your MySQL query statement below
select Department,Employee,Salary
from (
    select d.name as Department, e.name as Employee, e.salary as Salary ,dense_rank() over(
        partition by e.departmentId
        order by e.salary desc
    )"drank"
    from Employee e
    inner join Department d
    on e.departmentId = d.id
)y
where y.drank <= 3
