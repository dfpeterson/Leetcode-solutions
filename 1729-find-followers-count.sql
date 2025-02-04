/*
Level: Easy
Link: https://leetcode.com/problems/find-followers-count/
Tags: database
Description:
Write a solution that will, for each user, return the number of followers.

Return the result table ordered by user_id in ascending order.
*/
SELECT
    f.user_id,
    count(f.follower_id) AS followers_count
FROM
    followers AS f
GROUP BY
    f.user_id
ORDER BY
    f.user_id
