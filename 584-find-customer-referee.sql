/*
Level: Easy
Link: https://leetcode.com/problems/find-customer-referee/
Tags: database
Description:
Find the names of the customer that are not referred by the customer with
id = 2.

Return the result table in any order.
*/
SELECT c.name
FROM
    customer AS c
WHERE
    c.referee_id != 2
    OR c.referee_id IS NULL
