/*
Level: Easy
Link: https://leetcode.com/problems/bank-account-summary-ii/
Tags: database
Description:
Write a solution to report the name and balance of users with a balance higher
than 10000. The balance of an account is equal to the sum of the amounts of all
transactions involving that account.

Return the result table in any order.
*/
SELECT
    u.name,
    sum(t.amount) AS balance
FROM
    users AS u
INNER JOIN transactions AS t
    ON
        u.account = t.account
GROUP BY
    u.name
HAVING
    sum(t.amount) > 10000
