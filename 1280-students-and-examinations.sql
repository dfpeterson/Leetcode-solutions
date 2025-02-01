/*
Level: Easy
Link: https://leetcode.com/problems/students-and-examinations/
Tags: database
Description:
Write a solution to find the number of times each student attended each exam.

Return the result table ordered by student_id and subject_name.
*/
SELECT
    st.student_id,
    st.student_name,
    sj.subject_name,
    count(e.subject_name) AS attended_exams
FROM
    students AS st
INNER JOIN subjects AS sj
    ON
        1 = 1
LEFT JOIN examinations AS e
    ON
        st.student_id = e.student_id
        AND sj.subject_name = e.subject_name
GROUP BY
    st.student_id,
    st.student_name,
    sj.subject_name
