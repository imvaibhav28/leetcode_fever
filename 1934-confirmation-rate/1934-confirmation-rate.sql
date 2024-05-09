/* Write your PL/SQL query statement below */



select s.user_id, round( NVL(count(c3.action),0)/(case when count(c.action) = 0 then 1 else count(c.action) end) ,2) as confirmation_rate
from signups s left  outer join confirmations c on s.user_id=c.user_id
left join ( select * from confirmations c2 where c2.action = 'confirmed') c3
on c.user_id = c3.user_id and c.time_stamp=c3.time_stamp
group by s.user_id;
