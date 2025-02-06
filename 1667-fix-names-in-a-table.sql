/*
Level: Easy
Link: https://leetcode.com/problems/fix-names-in-a-table/
Tags: database
Description:
Write a solution to fix the names so that only the first character is uppercase
and the rest are lowercase.

Return the result table ordered by user_id.
*/
SELECT
    u.user_id,
    upper(substr(u.name, 1, 1)) || lower(substr(u.name, 2)) AS name
FROM
    users AS u
ORDER BY
    u.user_id
