/*
Level: Easy
Link: https://leetcode.com/problems/user-activity-for-the-past-30-days-i/
Tags: database
Description:
Write a solution to find the daily active user count for a period of 30 days
ending 2019-07-27 inclusively. A user was active on someday if they made at
least one activity on that day.

Return the result table in any order.
*/
SELECT
    a.activity_date AS day,
    count(DISTINCT a.user_id) AS active_users
FROM
    activity AS a
WHERE
    a.activity_date BETWEEN '2019-06-28' AND '2019-07-27'
GROUP BY
    a.activity_date
