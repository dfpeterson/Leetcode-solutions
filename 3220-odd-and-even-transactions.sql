/*
Level: Medium
Link: https://leetcode.com/problems/odd-and-even-transaction-amounts/
Tags: database
Description:
Write a solution to find the sum of amounts for odd and even transactions for
each day. If there are no odd or even transactions for a specific date, display
as 0.

Return the result table ordered by transaction_date in ascending order.
*/
SELECT
    t.transaction_date,
    coalesce(sum(t.amount) FILTER (
        WHERE t.amount % 2 = 1
    ),
    0) AS odd_sum,
    coalesce(sum(t.amount) FILTER (
        WHERE t.amount % 2 = 0
    ),
    0) AS even_sum
FROM
    transactions AS t
GROUP BY
    t.transaction_date
ORDER BY
    t.transaction_date
