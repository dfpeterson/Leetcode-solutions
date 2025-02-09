/*
Level: Medium
Link:
Tags: database
Description:
Write a solution to find the nth highest salary from the Employee table. If
there is no nth highest salary, return null.
*/
CREATE OR REPLACE FUNCTION NTHHIGHESTSALARY(N INT) RETURNS TABLE (
    Salary INT
) AS $$
BEGIN
  RETURN QUERY (
-- Write your PostgreSQL query statement below.
    WITH unique_employee AS (
SELECT
	e.salary
FROM
	employee e
GROUP BY
	e.salary
    )
SELECT
	lead(ue.salary,
	n-1) OVER (
	ORDER BY ue.salary DESC) AS getnthhighestsalary
FROM
	unique_employee ue
LIMIT 1
  );
END;

$$ LANGUAGE Plpgsql;
