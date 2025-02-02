/*
Level: Medium
Link: https://leetcode.com/problems/monthly-transactions-i/
Tags: database
Description:
Write an SQL query to find for each month and country, the number of
transactions and their total amount, the number of approved transactions and
their total amount.

Return the result table in any order.
*/
SELECT
    country,
    to_char(date_trunc(
        'month',
        trans_date
    ),
    'yyyy-mm') AS month,
    count(*) AS trans_count,
    coalesce(
        count(CASE WHEN state = 'approved' THEN id END),
        0
    ) AS approved_count,
    sum(amount) AS trans_total_amount,
    coalesce(
        sum(CASE WHEN state = 'approved' THEN amount ELSE 0 END),
        0
    ) AS approved_total_amount
FROM
    transactions
GROUP BY
    date_trunc(
        'month',
        trans_date
    ),
    country
