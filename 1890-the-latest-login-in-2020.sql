/*
Level: Easy
Link: https://leetcode.com/problems/the-latest-login-in-2020/
Tags: database
Description:
Write a solution to report the latest login for all users in the year 2020. Do
not include the users who did not login in 2020.

Return the result table in any order.
*/
SELECT
    l.user_id,
    max(l.time_stamp) AS last_stamp
FROM
    logins AS l
WHERE
    l.time_stamp BETWEEN '2020-01-01 00:00:00' AND '2020-12-31 23:59:59'
GROUP BY
    l.user_id
