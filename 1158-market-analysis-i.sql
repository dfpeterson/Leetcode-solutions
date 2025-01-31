/*
Level: Medium
Link: https://leetcode.com/problems/market-analysis-i/
Tags: database
Description:
Write a solution to find for each user, the join date and the number of orders
they made as a buyer in 2019.

Return the result table in any order.
*/
SELECT
    u.user_id AS buyer_id,
    MIN(u.join_date) AS join_date,
    COALESCE(
        COUNT(o.order_id),
        0
    ) AS orders_in_2019
FROM
    users AS u
LEFT JOIN orders AS o
    ON
        u.user_id = o.buyer_id
        AND o.order_date BETWEEN '2019-01-01' AND '2019-12-31'
GROUP BY
    u.user_id
