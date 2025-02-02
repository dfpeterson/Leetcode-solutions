/*
Level: Easy
Link: https://leetcode.com/problems/percentage-of-users-attended-a-contest/
Tags: database
Description:
Write a solution to find the percentage of the users registered in each contest
rounded to two decimals.

Return the result table ordered by percentage in descending order. In case of a
tie, order it by contest_id in ascending order.
*/
WITH user_count AS (
    SELECT count(*) AS total_users
    FROM
        users
)

SELECT
    r.contest_id,
    round(
        count(*) / uc.total_users::numeric * 100,
        2
    ) AS percentage
FROM
    register AS r
INNER JOIN user_count AS uc
    ON
        1 = 1
GROUP BY
    r.contest_id,
    uc.total_users
ORDER BY
    percentage DESC,
    r.contest_id ASC
