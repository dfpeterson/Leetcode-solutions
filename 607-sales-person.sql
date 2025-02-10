/*
Level: Easy
Link: https://leetcode.com/problems/sales-person/
Tags: database
Description:
Write a solution to find the names of all the salespersons who did not have any
orders related to the company with the name "RED".

Return the result table in any order.
*/
SELECT s.name
FROM
    salesperson AS s
LEFT JOIN orders AS o
    ON
        s.sales_id = o.sales_id
LEFT JOIN company AS c
    ON
        o.com_id = c.com_id
GROUP BY
    s.name
HAVING
    coalesce(
        count(CASE WHEN c.name = 'RED' THEN o.order_id END),
        0
    ) = 0
