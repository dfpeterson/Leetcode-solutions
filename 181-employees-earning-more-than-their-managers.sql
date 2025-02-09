/*
Level: Easy
Link: https://leetcode.com/problems/employees-earning-more-than-their-managers/
Tags: database
Description:
Write a solution to find the employees who earn more than their managers.

Return the result table in any order.
*/
SELECT e.name AS employee
FROM
    employee AS e
INNER JOIN employee AS m ON
    e.managerid = m.id
    AND e.salary > m.salary
