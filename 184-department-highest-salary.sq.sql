/*
Level: Medium
Link: https://leetcode.com/problems/department-highest-salary/
Tags: database
Description:
Write a solution to find employees who have the highest salary in each of the
departments.

Return the result table in any order.
*/
WITH ranked_sals AS (
    SELECT
        d.name AS department,
        e.name AS employee,
        e.salary,
        rank() OVER (
            PARTITION BY d.name
            ORDER BY
                e.salary DESC
        ) AS sal_rank
    FROM
        department AS d
    INNER JOIN employee AS e ON
        d.id = e.departmentid
)

SELECT
    department,
    employee,
    salary
FROM
    ranked_sals
WHERE
    sal_rank = 1
