/*
Level: Easy
Link: https://leetcode.com/problems/employee-bonus/
Tags: database
Description:
Write a solution to report the name and bonus amount of each employee with a
bonus less than 1000.

Return the result table in any order.
*/
SELECT
    e.name,
    b.bonus
FROM
    employee AS e
LEFT JOIN bonus AS b
    ON
        e.empid = b.empid
WHERE
    b.bonus < 1000
    OR b.bonus IS null
