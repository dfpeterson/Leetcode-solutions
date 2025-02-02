/*
Level: Easy
Link: https://leetcode.com/problems/queries-quality-and-percentage/
Tags: database
Description:
We define query quality as:
 * The average of the ratio between query rating and its position.

We also define poor query percentage as:
 * The percentage of all queries with rating less than 3.

Write a solution to find each query_name, the quality and
poor_query_percentage.

Both quality and poor_query_percentage should be rounded to 2 decimal places.

Return the result table in any order.
*/
WITH clean_queries AS (
    SELECT
        q.query_name,
        q.result,
        q.position,
        q.rating
    FROM
        queries AS q
    GROUP BY
        q.query_name,
        q.result,
        q.position,
        q.rating
)

SELECT
    query_name,
    round(
        avg(rating::numeric / position::numeric),
        2
    ) AS quality,
    round(
        100 * sum(CASE WHEN rating < 3 THEN 1 ELSE 0 END) / count(*)::numeric,
        2
    ) AS poor_query_percentage
FROM
    clean_queries
GROUP BY
    query_name
