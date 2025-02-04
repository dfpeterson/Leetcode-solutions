/*
Level: Easy
Link: https://leetcode.com/problems/employees-with-missing-information/
Tags: database
Description:
Write a solution to report the IDs of all the employees with missing
information. The information of an employee is missing if:
 * The employee's name is missing, or
 * The employee's salary is missing.

Return the result table ordered by employee_id in ascending order.
*/
SELECT
    coalesce(
        e.employee_id,
        s.employee_id
    ) AS employee_id
FROM
    employees AS e
FULL JOIN salaries AS s
    ON
        e.employee_id = s.employee_id
WHERE
    e.name IS null
    OR s.salary IS null
ORDER BY
    coalesce(
        e.employee_id,
        s.employee_id
    )
