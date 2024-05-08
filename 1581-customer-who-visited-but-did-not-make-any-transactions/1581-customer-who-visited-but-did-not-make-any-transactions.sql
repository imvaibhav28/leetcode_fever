/* Write your PL/SQL query statement below */


select customer_id, count(visit_id) as count_no_trans
from Visits
where visit_id in (
select visit_id from Visits 
minus
select visit_id from Transactions )
group by customer_id;