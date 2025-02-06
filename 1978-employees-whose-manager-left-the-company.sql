/*
Level: Easy
Link: https://leetcode.com/problems/employees-whose-manager-left-the-company/
Tags: database
Description:
Find the IDs of the employees whose salary is strictly less than $30000 and
whose manager left the company. When a manager leaves the company, their
information is deleted from the Employees table, but the reports still have
their manager_id set to the manager that left.

Return the result table ordered by employee_id.
*/
SELECT e.employee_id
FROM
    employees AS e
WHERE
    e.salary < 30000
    AND e.manager_id IS NOT null
    AND NOT EXISTS (
        SELECT 1
        FROM
            employees AS e2
        WHERE
            e.manager_id = e2.employee_id
    )
ORDER BY
    e.employee_id
