/*
Level: Easy
Link: https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/
Tags: database
Description:
Write a solution to find the IDs of the users who visited without making any
transactions and the number of times they made these types of visits.

Return the result table sorted in any order.
*/
SELECT
    v.customer_id,
    COUNT(*) AS count_no_trans
FROM
    visits AS v
LEFT JOIN transactions AS t
    ON
        v.visit_id = t.visit_id
WHERE
    t.visit_id IS NULL
GROUP BY
    v.customer_id
