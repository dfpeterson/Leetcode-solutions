/*
Level: Easy
Link: https://leetcode.com/problems/classes-more-than-5-students/
Tags: database
Description:
Write a solution to find all the classes that have at least five students.

Return the result table in any order.
*/
SELECT c.class
FROM
    courses AS c
GROUP BY
    c.class
HAVING
    count(*) >= 5
