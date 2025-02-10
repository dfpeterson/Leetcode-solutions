/*
Level: Easy
Link: https://leetcode.com/problems/game-play-analysis-i/
Tags: database
Description:
Write a solution to find the first login date for each player.

Return the result table in any order.
*/
SELECT
    a.player_id,
    min(a.event_date) AS first_login
FROM
    activity AS a
GROUP BY
    a.player_id
