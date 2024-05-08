/* Write your PL/SQL query statement below */




select machine_id, round(sum(p_time)/count(process_id),3) as processing_time
from (
select a1.machine_id,a1.process_id, a2.timestamp-a1.timestamp p_time
from activity a1 inner join activity a2
on a1.machine_id=a2.machine_id and a1.process_id=a2.process_id
where a1.activity_type ='start' and a2.activity_type='end'
)
group by machine_id;
