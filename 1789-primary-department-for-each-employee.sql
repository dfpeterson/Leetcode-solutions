/*
Level: Easy
Link: https://leetcode.com/problems/primary-department-for-each-employee/
Tags: database
Description:
Employees can belong to multiple departments. When the employee joins other
departments, they need to decide which department is their primary department.
Note that when an employee belongs to only one department, their primary column
is 'N'.

Write a solution to report all the employees with their primary department. For
employees who belong to one department, report their only department.

Return the result table in any order.
*/
WITH ranked_job AS (
    SELECT
        e.employee_id,
        e.department_id,
        row_number() OVER (
            PARTITION BY e.employee_id
            ORDER BY
                e.primary_flag DESC
        ) AS job_order
    FROM
        employee AS e
)

SELECT
    employee_id,
    department_id
FROM
    ranked_job
WHERE
    job_order = 1
