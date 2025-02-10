/*
Level: Easy
Link: https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/
Tags: database
Description:
Write a solution to find the customer_number for the customer who has placed
the largest number of orders.

The test cases are generated so that exactly one customer will have placed more
orders than any other customer.
*/
SELECT o.customer_number
FROM
    orders AS o
GROUP BY
    o.customer_number
ORDER BY
    count(o.order_number) DESC
LIMIT 1
