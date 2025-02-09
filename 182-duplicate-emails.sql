/*
Level: Easy
Link: https://leetcode.com/problems/duplicate-emails/
Tags: database
Description:
Write a solution to report all the duplicate emails. Note that it's guaranteed
that the email field is not NULL.

Return the result table in any order.
*/
SELECT p.email
FROM
    person AS p
GROUP BY
    p.email
HAVING
    count(p.email) > 1
