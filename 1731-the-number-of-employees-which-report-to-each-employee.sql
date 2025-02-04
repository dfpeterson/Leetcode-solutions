/*
Level: Easy
Link: https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/
Tags: database
Description:
For this problem, we will consider a manager an employee who has at least 1
other employee reporting to them.

Write a solution to report the ids and the names of all managers, the number
of employees who report directly to them, and the average age of the reports
rounded to the nearest integer.

Return the result table ordered by employee_id.
*/
SELECT
    e1.employee_id,
    e1.name,
    count(*) AS reports_count,
    round(avg(e2.age)) AS average_age
FROM
    employees AS e1
INNER JOIN employees AS e2
    ON
        e1.employee_id = e2.reports_to
GROUP BY
    e1.employee_id,
    e1.name
ORDER BY
    e1.employee_id
