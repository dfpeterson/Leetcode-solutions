/*
Level: Easy
Link: https://leetcode.com/problems/triangle-judgement/
Tags: database
Description:
Report for every three line segments whether they can form a triangle.

Return the result table in any order.
*/
SELECT
    t.x,
    t.y,
    t.z,
    CASE
        WHEN
            t.x + t.y > t.z
            AND t.y + t.z > t.x
            AND t.x + t.z > t.y THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM
    triangle AS t
