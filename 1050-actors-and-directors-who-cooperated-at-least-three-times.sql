/*
Level: Easy
Link: https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/
Tags: database
Description:
Write a solution to find all the pairs (actor_id, director_id) where the actor
has cooperated with the director at least three times.

Return the result table in any order.
*/
SELECT
    ad.actor_id,
    ad.director_id
FROM
    actordirector AS ad
GROUP BY
    ad.actor_id,
    ad.director_id
HAVING
    COUNT(ad.timestamp) > 2
