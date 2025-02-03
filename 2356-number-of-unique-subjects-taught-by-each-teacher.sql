/*
Level: Easy
Link: https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/
Tags: database
Description:
Write a solution to calculate the number of unique subjects each teacher
teaches in the university.

Return the result table in any order.
*/
SELECT
    t.teacher_id,
    count(DISTINCT t.subject_id) AS cnt
FROM
    teacher AS t
GROUP BY
    t.teacher_id
