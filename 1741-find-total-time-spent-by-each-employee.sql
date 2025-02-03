/*
Level: Easy
Link: https://leetcode.com/problems/find-total-time-spent-by-each-employee/
Tags: database
Description:
Write a solution to calculate the total time in minutes spent by each employee
on each day at the office. Note that within one day, an employee can enter and
leave more than once. The time spent in the office for a single entry is
out_time - in_time.

Return the result table in any order.
*/
SELECT
    e.event_day AS day,
    e.emp_id,
    sum(e.out_time - e.in_time) AS total_time
FROM employees AS e
GROUP BY e.event_day, e.emp_id
