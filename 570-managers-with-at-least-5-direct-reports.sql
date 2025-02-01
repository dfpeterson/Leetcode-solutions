/*
Level: Medium
Link: https://leetcode.com/problems/managers-with-at-least-5-direct-reports/
Tags: database
Description:
Write a solution to find managers with at least five direct reports.

Return the result table in any order.
*/
SELECT e2.name
FROM
    employee AS e1
INNER JOIN employee AS e2
    ON
        e1.managerid = e2.id
GROUP BY
    e2.name,
    e2.id
HAVING
    count(e1.id) >= 5
