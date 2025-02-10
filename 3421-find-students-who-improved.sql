/*
Level: Medium
Link: https://leetcode.com/problems/find-students-who-improved/
Tags: database
Description:
Write a solution to find the students who have shown improvement. A student is
considered to have shown improvement if they meet both of these conditions:
 * Have taken exams in the same subject on at least two different dates
 * Their latest score in that subject is higher than their first score

Return the result table ordered by student_id, subject in ascending order.
*/
WITH score_change AS (
    SELECT
        s.student_id,
        s.subject,
        first_value(s.score) OVER (
            PARTITION BY
                s.student_id,
                s.subject
            ORDER BY
                s.exam_date
        ) AS first_score,
        first_value(s.score) OVER (
            PARTITION BY
                s.student_id,
                s.subject
            ORDER BY
                s.exam_date DESC
        ) AS latest_score
    FROM
        scores AS s
)

SELECT
    student_id,
    subject,
    first_score,
    latest_score
FROM
    score_change
WHERE
    latest_score > first_score
GROUP BY
    student_id,
    subject,
    first_score,
    latest_score
ORDER BY
    student_id,
    subject
