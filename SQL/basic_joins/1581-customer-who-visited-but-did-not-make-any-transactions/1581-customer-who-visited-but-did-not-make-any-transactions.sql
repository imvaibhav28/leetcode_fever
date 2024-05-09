/* Write your PL/SQL query statement below */


-- select customer_id, count(visit_id) as count_no_trans
-- from Visits
-- where visit_id in (
-- select visit_id from Visits 
-- minus
-- select visit_id from Transactions )
-- group by customer_id;

-- SELECT customer_id, COUNT(visit_id) as count_no_trans 
-- FROM Visits
-- WHERE visit_id NOT IN (
-- 	SELECT visit_id FROM Transactions
-- 	)
-- GROUP BY customer_id

SELECT customer_id, COUNT(v.visit_id) as count_no_trans 
FROM Visits v
LEFT JOIN Transactions t ON v.visit_id = t.visit_id
WHERE transaction_id IS NULL
GROUP BY customer_id