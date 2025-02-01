/*
Level: Easy
Link: https://leetcode.com/problems/top-travellers/
Tags: database
Description:
Write a solution to report the distance traveled by each user.

Return the result table ordered by travelled_distance in descending order, if
two or more users traveled the same distance, order them by their name in
ascending order.
*/
SELECT
    u.name,
    coalesce(
        sum(r.distance),
        0
    ) AS traveled_distance
FROM
    users AS u
LEFT JOIN rides AS r
    ON
        u.id = r.user_id
GROUP BY
    u.name
ORDER BY
    traveled_distance DESC,
    u.name ASC
