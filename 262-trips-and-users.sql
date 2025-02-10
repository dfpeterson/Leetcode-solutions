/*
Level: Hard
Link: https://leetcode.com/problems/trips-and-users/
Tags: database
Description:
The cancellation rate is computed by dividing the number of canceled (by client
or driver) requests with unbanned users by the total number of requests with
unbanned users on that day.

Write a solution to find the cancellation rate of requests with unbanned users
(both client and driver must not be banned) each day between "2013-10-01" and
"2013-10-03". Round Cancellation Rate to two decimal points.

Return the result table in any order.
*/
WITH drive_days AS (
    SELECT '2013-10-01' AS day
    UNION ALL
    SELECT '2013-10-02'
    UNION ALL
    SELECT '2013-10-03'
)

SELECT
    dd.day,
    round(coalesce(
        avg(CASE WHEN t.status != 'completed' THEN 1 ELSE 0 END),
        0
    ),
    2) AS "cancellation rate"
FROM
    drive_days AS dd
LEFT JOIN trips AS t
    ON
        dd.day = t.request_at
WHERE
    t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
    AND EXISTS (
        SELECT 1
        FROM
            users AS u
        WHERE
            u.users_id = t.client_id
            AND u.banned = 'No'
            AND u.role = 'client'
    )
    AND EXISTS (
        SELECT 1
        FROM
            users AS u
        WHERE
            u.users_id = t.driver_id
            AND u.banned = 'No'
            AND u.role = 'driver'
    )
GROUP BY
    dd.day
