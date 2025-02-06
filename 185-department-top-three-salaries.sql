/*
Level: Medium
Link: https://leetcode.com/problems/department-top-three-salaries/
Tags: database
Description:
A company's executives are interested in seeing who earns the most money in
each of the company's departments. A high earner in a department is an employee
who has a salary in the top three unique salaries for that department.

Write a solution to find the employees who are high earners in each of the
departments.

Return the result table in any order.
*/
WITH ranked_sals AS (
    SELECT
        d.name AS department,
        e.name AS employee,
        e.salary,
        dense_rank() OVER (
            PARTITION BY e.departmentid
            ORDER BY
                e.salary DESC
        ) AS sal_rank
    FROM
        employee AS e
    INNER JOIN department AS d ON
        e.departmentid = d.id
)

SELECT
    department,
    employee,
    salary
FROM
    ranked_sals
WHERE
    sal_rank <= 3
