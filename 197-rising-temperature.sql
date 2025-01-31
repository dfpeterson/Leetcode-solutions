/*
Level: Easy
Link: https://leetcode.com/problems/rising-temperature/
Tags: database
Description:
Write a solution to find all dates' id with higher temperatures compared to its
previous dates (yesterday).

Return the result table in any order.
*/
WITH temp_change AS (
    SELECT
        id,
        COALESCE((temperature > LAG(temperature) OVER (
            ORDER BY recorddate
        ))
        AND (recorddate = LAG(recorddate) OVER (
            ORDER BY recorddate
        ) + interval '1 day'),
        FALSE) AS temp_increase
    FROM
        weather
)

SELECT id
FROM
    temp_change
WHERE
    temp_increase
