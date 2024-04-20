# Write your MySQL query statement below


select name
from Customer
where name not in (select name from customer where referee_id = 2)