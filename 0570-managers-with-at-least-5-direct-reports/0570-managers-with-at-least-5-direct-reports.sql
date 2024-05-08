/* Write your PL/SQL query statement below */

select name from (
select e1.name,e1.id
from Employee e1 inner join Employee e2
on e1.id = e2.managerId
group by e1.id,e1.name
having count(e1.id)>=5)
;