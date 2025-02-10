/*
Level: Easy
Link: https://leetcode.com/problems/customers-who-never-order/
Tags: database
Description:
Write a solution to find all customers who never order anything.

Return the result table in any order.
*/
SELECT c.name AS customers
FROM
    customers AS c
WHERE
    NOT EXISTS (
        SELECT 1
        FROM
            orders AS o
        WHERE
            o.customerid = c.id
    )
