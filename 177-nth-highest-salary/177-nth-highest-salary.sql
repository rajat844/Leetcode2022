CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
declare m int;
set m = N-1;
  RETURN (
      # Write your MySQL query statement below.
      select nullif(
          (select distinct salary 
           from employee
           order by salary desc
           limit m,1
              
          ),null) as getNthHighestSalary
  );
END