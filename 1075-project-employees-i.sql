/*
Level: Easy
Link: https://leetcode.com/problems/project-employees-i/
Tags: database
Description:
Write an SQL query that reports the average experience years of all the
employees for each project, rounded to 2 digits.

Return the result table in any order.
*/
SELECT
    p.project_id,
    round(
        avg(e.experience_years)::numeric,
        2
    ) AS average_years
FROM
    project AS p
INNER JOIN employee AS e
    ON
        p.employee_id = e.employee_id
GROUP BY
    p.project_id
