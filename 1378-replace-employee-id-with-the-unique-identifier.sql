/*
Level: Easy
Link: https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/
Tags: database
Description:
Write a solution to show the unique ID of each user, If a user does not have a
unique ID replace just show null.

Return the result table in any order.
*/
SELECT
    eu.unique_id,
    e.name
FROM
    employees AS e
LEFT JOIN employeeuni AS eu ON
    e.id = eu.id
