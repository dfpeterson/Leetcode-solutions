/*
Level: Medium
Link: https://leetcode.com/problems/second-highest-salary/
Tags: database
Description:
Write a solution to find the second highest distinct salary from the Employee
table. If there is no second highest salary, return null (return None in
Pandas).
*/
SELECT secondhighestsalary
FROM
    (
        SELECT
            lead(e.salary) OVER (
                ORDER BY e.salary DESC
            ) AS secondhighestsalary
        FROM
            employee AS e
        GROUP BY
            e.salary
        UNION ALL
        SELECT null
    )
LIMIT 1
