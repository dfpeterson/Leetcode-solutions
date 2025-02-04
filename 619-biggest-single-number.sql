/*
Level: Easy
Link: https://leetcode.com/problems/biggest-single-number/
Tags: database
Description:
A single number is a number that appeared only once in the MyNumbers table.

Find the largest single number. If there is no single number, report null.
*/
WITH top_num AS (
    SELECT
        m.num,
        count(*) AS num_count
    FROM
        mynumbers AS m
    GROUP BY
        m.num
)

SELECT
    CASE
        WHEN num_count = 1 THEN num
    END AS num
FROM
    top_num
ORDER BY
    num_count ASC,
    num DESC
LIMIT 1
