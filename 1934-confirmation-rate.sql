/*
Level: Medium
Link: https://leetcode.com/problems/confirmation-rate/
Tags: database
Description:
The confirmation rate of a user is the number of 'confirmed' messages divided
by the total number of requested confirmation messages. The confirmation rate
of a user that did not request any confirmation messages is 0. Round the
confirmation rate to two decimal places.

Write a solution to find the confirmation rate of each user.

Return the result table in any order.
*/
WITH confirm_count AS (
    SELECT
        s.user_id,
        sum(CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END) AS is_confirmed,
        count(c.action) AS actions
    FROM
        signups AS s
    LEFT JOIN confirmations AS c
        ON
            s.user_id = c.user_id
    GROUP BY
        s.user_id
)

SELECT
    user_id,
    CASE
        WHEN actions > 0
            THEN round(
                is_confirmed / actions::numeric,
                2
            )
        ELSE 0::float
    END AS confirmation_rate
FROM
    confirm_count
