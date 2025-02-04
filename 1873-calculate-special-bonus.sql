/*
Level: Easy
Link: https://leetcode.com/problems/calculate-special-bonus/
Tags: database
Description:
Write a solution to calculate the bonus of each employee. The bonus of an
employee is 100% of their salary if the ID of the employee is an odd number and
the employee's name does not start with the character 'M'. The bonus of an
employee is 0 otherwise.

Return the result table ordered by employee_id.
**/
SELECT
    e.employee_id,
    CASE
        WHEN
            e.employee_id % 2 = 1
            AND e.name NOT ILIKE 'm%' THEN e.salary
        ELSE 0
    END AS bonus
FROM
    employees AS e
ORDER BY
    e.employee_id
